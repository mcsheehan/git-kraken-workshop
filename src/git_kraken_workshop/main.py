from fastapi import FastAPI

app = FastAPI()


@app.get("/richard/{subordinate}")
async def get_richard(subordinate: str):
    if subordinate == "faheem":
        return {"message": "failed probation"}

    return {"message": f"Hello {subordinate}"}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
