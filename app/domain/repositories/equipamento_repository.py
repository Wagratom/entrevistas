from app.infrastructure.db.models import UserModel
from app.infrastructure.db.database import db
from app.domain.interfaces.equipamento_repository import EquipamentoRepositoryInterface

class UserRepositoryImpl(EquipamentoRepositoryInterface):
    def save(self, user):
        user_model = UserModel(username=user.username, email=user.email)
        db.session.add(user_model)
        db.session.commit()
