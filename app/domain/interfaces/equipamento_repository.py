from abc import ABC, abstractmethod
from app.domain.entities.equipamentos import Equipamento

class EquipamentoRepositoryInterface(ABC):

    @abstractmethod
    def save(self, user: Equipamento):
        pass

