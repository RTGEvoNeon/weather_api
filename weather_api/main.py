import fastapi
import jinja2
import uvicorn
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from api import weather_api
from views import home


def configure_routing():
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)

def configure():
    configure_routing()


api = fastapi.FastAPI()

if __name__ == '__main__':
    configure()
    uvicorn.run(api)
else:
    configure()