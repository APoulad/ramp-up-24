from fastapi import FastAPI

server = FastAPI()


@server.get('/{name}')
async def print_name(name):
    msg = "Hello " + name
    return msg
