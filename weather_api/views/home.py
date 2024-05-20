import fastapi
import jinja2
import uvicorn
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from starlette.requests import Request

router = fastapi.APIRouter()
templates = Jinja2Templates('templates')

@router.get('/favicon.ico')
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {"request": request})
