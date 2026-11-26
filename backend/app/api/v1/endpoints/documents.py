from fastapi import APIRouter, Query
from app.schemas.common import PaginationResponse

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.get("", response_model = PaginationResponse)
def list_documents(
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
):
    return{
        "items": [],
        "page": page,
        "limit": limit,
        "total": 0,
        "total_pages": 0,
    }