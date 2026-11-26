from pydanticmodel import BaseModel 

class DocumentResponse(BaseModel):
    id: str
    name: str
    description: str | None
    content_type: str
    size: int
    folder_id: str | None
    created_at: str
    created_by: str
    status: str        