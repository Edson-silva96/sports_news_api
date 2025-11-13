from pydantic import BaseModel
from typing import List, Union

class noticia(BaseModel):
    titulo: str
    comentario: str
    link: str