from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from ..models.council import Council
from ..models import db

router = APIRouter()


class CouncilModel(BaseModel):
    council_id: int
    council_name: str
    region_id: int
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


Items = List[CouncilModel]


@router.get("/", response_model=Items)
async def get_all_councils():
    result = await db.all(Council.query)
    return result


@router.get("/{id}")
async def get_council(id: int):
    result = await Council.get_or_404(id)
    return result.to_dict()
