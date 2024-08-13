# app/infrastructure/web/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from app.domain.services.equipamento_service import UserService
from app.infrastructure.web.validators.user_validator import UserValidator
from app.domain.entities.equipamentos import Equipamento

equipamento_bp = Blueprint('equipamento', __name__)
user_service = UserService()

@equipamento_bp.route('/register', methods=['POST'])
def register_user():
    form = UserValidator(request.form)
    if form.validate():
        user = Equipamento(**form)
        user_service.register_user(user)
        return jsonify({"message": "User registered successfully"}), 201
    return jsonify(form.errors), 400
