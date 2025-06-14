from fastapi import FastAPI

app = FastAPI()

# app = FastAPI(
#     docs_url="/docs",
#     redoc_url=None,  # 禁用 ReDoc
# )

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}