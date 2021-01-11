from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


# access_token 받아오기
@router.get("/authorize")
def get_access_token() -> Any:
    return


# OAuth  목록 가져오기 - Token
@router.get("/")
def get_app_list() -> Any:
    return


# OAuth 클라이언트 생성 - Token
@router.post("/")
def create_oauth_client():
    return


# OAuth 클라이언트 삭제
@router.delete("/")
def delete_oauth_client():
    return