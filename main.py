import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    return fastapi.Response(content='Ты не туда идешь!')

@api.get('/api/calculate')
def calculate(x: int, y: int):
    value = x + y
    if value < 3:
        return fastapi.Response(content='У нас великая малютка!', status_code=400, media_type='application/json')
    elif value > 10:
        return fastapi.responses.JSONResponse(content={"error": "Я боюсь темноты"}, status_code=400)
    return {
        'result': value
    }

uvicorn.run(api, port=8000, host='127.0.0.1')
