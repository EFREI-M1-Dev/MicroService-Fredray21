from pydantic import BaseModel
from typing import List, Optional

# Model for Cast for creating a new cast
class CastIn(BaseModel):
    name: str
    nationality: Optional[str] = None


# Model for Cast for returning a cast
class CastOut(CastIn):
    id: int

# Model for Cast for updating a cast
class CastUpdate(CastIn):
    name: Optional[str] = None
