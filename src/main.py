import uvicorn
from fastapi import FastAPI

from config import APP_HOST, APP_PORT
from api.routers import all_routers


app = FastAPI(
    title="Task"
)


for router in all_routers:
    app.include_router(router)


def main():
    uvicorn.run(
        'main:app',
        proxy_headers=True,
        forwarded_allow_ips='*',
        host=APP_HOST,
        port=APP_PORT,
        reload=True,
    )


if __name__ == '__main__':
    main()
