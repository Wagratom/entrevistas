from pydantic import BaseModel

class Equipamento(BaseModel):
    nome: str
    tipo: str
    preco: float
    quantidade: int
