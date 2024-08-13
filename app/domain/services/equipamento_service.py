from app.domain.interfaces.equipamento_service import EquipamentoServiceInterface
from app.domain.interfaces.equipamento_repository import EquipamentoRepositoryInterface

from app.domain.entities.equipamentos import Equipamento
class UserService(EquipamentoServiceInterface):
    def __init__(self, repository: EquipamentoRepositoryInterface):
        self.repository = repository

    def register(self, equipamentoData: Equipamento):
        equipamento = Equipamento(equipamentoData)   
