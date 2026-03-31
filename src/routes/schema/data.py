from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int]=100
    over_lap: Optional[int] = 5
    do_reset: Optional[int] = 1