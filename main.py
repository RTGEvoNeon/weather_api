import fastapi
import uvicorn
api = fastapi.FastAPI()

@api.get('/api/calculate')
def calculate(x:int, y:int):
    value = x + y
    return {
        'result': value
    }


uvicorn.run(api, port=8000, host='127.0.0.1')
