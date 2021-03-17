from fastapi import APIRouter
from Data.connection import Table


router = APIRouter(prefix="/api/v1/badges",  tags=["badges"])


@router.get("/")
async def get_badges():
    table = Table('badges')
    data = table.query()
    return data.items


@router.get("/{item_id}")
async def get_badge(item_id: int):
    table = Table('badges')
    item = table.query('RowKey', f'{item_id}')
    return item.items[0]