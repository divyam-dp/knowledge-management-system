from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter, Query, status
from app.schemas.common import PaginationResponse
from app.schemas.documents import DocumentCreateRequest, DocumentResponse
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
    
@router.post("", 
             response_model=DocumentResponse,
             status_code=status.HTTP_201_CREATED,
)
def create_documents(payload:DocumentCreateRequest):
    document = {
        "id": str(uuid4()),
        "name": payload.name,
        "description": payload.description,
        "content_type": payload.content_type,
        "size": payload.size,
        "folder_id": payload.folder_id,
        "created_at": datetime.now(timezone.utc),
        "created_by": "EMP001",
        "status": "active"
    }
    
    return document