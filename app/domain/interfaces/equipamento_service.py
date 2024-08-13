from abc import ABC, abstractmethod
from app.domain.entities.equipamentos import Equipamento

class EquipamentoServiceInterface(ABC):

    @abstractmethod()
    def register(self, equipamentoData: Equipamento):
        pass
