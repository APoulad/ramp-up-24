from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis

app = FastAPI()
r = redis.Redis(host='localhost', port=6379)

class Message(BaseModel):
    text: str

@app.post('/publish')
async def publish(message: Message):
    try:
        r.publish('my_channel', message.text)
        return {"message": "Message published"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))