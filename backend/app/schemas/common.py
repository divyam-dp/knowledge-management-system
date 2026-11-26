from pydantic import BaseModel

class PaginationResponse(BaseModel):
    items: list
    page: int
    limit: int
    total: int
    total_pages: int