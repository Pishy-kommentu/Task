from fastapi import APIRouter, HTTPException
from shemas.task import AddOrUpdateAddress, Response
from redis.redis import REDIS

router = APIRouter()


@router.get("/check_data")
async def check_data(phone: str):
    address = await REDIS.get_value(phone)

    if address is None:
        raise HTTPException(status_code=404, detail="Phone not found")

    return {"phone": phone, "address": address}


@router.post(
    "/write_data",
    response_model=Response,
    summary='Create address',
    status_code=201
)
async def write_data(request: AddOrUpdateAddress):
    address_obj = await REDIS.get_value(request.phone)
    if address_obj:
        raise HTTPException(
            status_code=422, detail="Address already exists"
        )
    await REDIS.set_value(request.phone, request.address)
    return Response(phone=request.phone, address=request.address)


@router.put(
    "/write_data",
    response_model=Response,
    summary='Update address',
    status_code=200
)
async def update_data(request: AddOrUpdateAddress):
    address_obj = await REDIS.get_value(request.phone)

    if address_obj is None:
        raise HTTPException(
            status_code=404, detail="Phone not found"
        )
    await REDIS.update_value(request.phone, request.address)

    return Response(phone=request.phone, address=request.address)
