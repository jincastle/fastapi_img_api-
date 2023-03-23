import logging

import uvicorn
from fastapi import FastAPI
from sqlalchemy import text

from config import get_env
from app.db.connection import db
from app.api.user_api import user

# 앱을 실행
def start_app():
    app = FastAPI(debug=True)
    env = get_env()
    # for i in env.__dict__.items():
    #     print(i)
    # print()
    db.init_db(app=app, **env.dict())
    get_session = db.session
    session = next(get_session()) # 제너레이터
    print(session.query(text("select 1")))

    app.include_router(user, prefix="/users", tags=["Users"])
    return app


if __name__ == "__main__":
    uvicorn.run("main:start_app", host="0.0.0.0", port=8000, reload=True, factory=True)