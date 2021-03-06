from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello world"}

@app.get("/{name}")
async def read_root_with_name(name: str):
    return {"message": f"Hello {name}"}