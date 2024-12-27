from fastapi import APIRouter


router = APIRouter()
@router.get('/')
@router.get('/home')
async def func_home():
    return {'message': "Hello this is the website for basic RAG simulation"}