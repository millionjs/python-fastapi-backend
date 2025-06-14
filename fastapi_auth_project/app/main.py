from fastapi import FastAPI
from app.routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# app = FastAPI(
#     docs_url="/docs",
#     redoc_url=None,  # 禁用 ReDoc
# )

ENV = os.getenv("ENV", "development")

if ENV == "production":
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI(docs_url="/docs", redoc_url="/redoc")

# 路由注册
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Auth Project"}