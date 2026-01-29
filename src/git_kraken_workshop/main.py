from fastapi import FastAPI

app = FastAPI()


@app.get("/max/{factory}")
async def get_maxs_factory(factory_name: str):
    return {"message": f"Hello and welcome to the factory {factory_name}"}


@app.get("/richard/{subordinate}")
async def get_richard(subordinate: str):
    return {"message": f"Hello {subordinate}"}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
