from fastapi import APIRouter, Depends
from starlette.requests import Request

router = APIRouter()


@router.post("/predict", response_model=None, name="predict")
def post_predict(
    request: Request,
    data,
):
    pass
