# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者 Windows:
# venv\Scripts\activate

# 安装 fastapi 和 uvicorn（ASGI 服务器）
[//]: # (pip install fastapi uvicorn)
pip install -r requirements.txt

✅ 步骤 3：启动服务
uvicorn main:app --reload


访问：http://localhost:8000
访问：http://127.0.0.1:8000/docs#/
访问：http://127.0.0.1:8000/redoc


📚 学习资源推荐
FastAPI 官方文档：https://fastapi.tiangolo.com
Pydantic 文档（用于数据验证）：https://docs.pydantic.dev
Uvicorn 文档：https://www.starlette.io/ or https://uvicorn.org


✅ 步骤 4：访问文档和接口
打开浏览器访问以下两个自动生成的文档页面：

Swagger UI : http://127.0.0.1:8000/docs
ReDoc : http://127.0.0.1:8000/redoc
你也可以直接调用接口：

http://127.0.0.1:8000/
http://127.0.0.1:8000/items/5?q=test