from fastapi import FastAPI

app = FastAPI()


@app.post("/health")
def read_root():
    return {"status": "ok"}




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}