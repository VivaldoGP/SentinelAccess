from fastapi import APIRouter
from ..utils.auth import openeo_auth

router = APIRouter()

@router.post("/auth")
async def auth(auth_option):
    connection = openeo_auth(option=auth_option)

    return "si jaló"