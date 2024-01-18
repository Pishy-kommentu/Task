from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints


class AddOrUpdateAddress(BaseModel):
    phone: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            pattern=r"^\+?[1-9]\d{1,14}$"
        )
    ]
    address: str


class Response(BaseModel):
    phone: str
    address: str
