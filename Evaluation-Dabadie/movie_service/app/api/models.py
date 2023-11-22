from pydantic import BaseModel
from typing import List, Optional

# donné de l'API d'acteur (acteur_service) d'entrée
class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts_id: List[int]

# donné de l'API d'acteur (acteur_service) de sortie
class MovieOut(MovieIn):
    id: int

#  donné de l'API d'acteur (acteur_service) de mise à jour
class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts_id: Optional[List[int]] = None
