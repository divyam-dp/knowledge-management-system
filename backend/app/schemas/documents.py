from pydantic import BaseModel, Field
from datetime import datetime

class DocumentCreateRequest(BaseModel):
    name: str = Field(min=1, max=255)
    description: str | None = None
    content_type: str
    size: int = Field(ge=0)
    folder_id: str | None = None
            
class DocumentResponse(BaseModel):
    id: str
    name: str = Field(min=1, max=255) #prevents empty doc name
    description: str | None = None
    content_type: str
    size: int = Field(ge=0)#prevents negative file size
    folder_id: str | None = None
    created_at: datetime
    created_by: str
    status: str        