from fastapi import FastAPI
from app.routers import product, recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product.router, prefix="/product", tags=["Products"])
app.include_router(recommend.router, prefix="/recommend", tags=["Recommend"])


@app.get("/health")
def read_root():
    return {"status": "ok"}

