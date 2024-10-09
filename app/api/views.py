from flask import Blueprint, jsonify, request
from app.extensions import db
from .models import User, Handicap, Treatment, Vaccination, HealthFolder, Address, MedicalExamination, Pro, Result

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    """
    Récupère les informations de l'utilisateur ainsi que les données associées par ID.
    """
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    # Récupérer les informations de l'utilisateur
    user_data = {
        "id": user.id,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "birth_date": user.birth_date,
        "weight": user.weight,
        "height": user.height,
        "gender": user.gender,
        "additional_infos": user.additional_infos,
        "address": {
            "zip_code": user.address.zip_code,
            "city": user.address.city,
            "street": user.address.street,
            "street_number": user.address.street_number,
            "appt_number": user.address.appt_number
        } if user.address else None,
        "handicaps": [
            {
                "id": handicap.id,
                "name": handicap.name,
                "is_temporary": handicap.is_temporary,
                "is_hereditary": handicap.is_hereditary,
                "is_physical": handicap.is_physical,
                "is_mental": handicap.is_mental
            } for handicap in user.handicaps
        ],
        "treatments": [
            {
                "id": treatment.id,
                "medication_name": treatment.medication_name,
                "dosage": treatment.dosage,
                "prescription_date": treatment.prescription_date,
                "duration_day": treatment.duration_day
            } for treatment in user.treatments
        ],
        "vaccinations": [
            {
                "id": vaccination.id,
                "vaccin_name": vaccination.vaccin_name,
                "date": vaccination.date,
                "recall_date": vaccination.recall_date
            } for vaccination in user.vaccinations
        ],
        "health_folder": {
            "id": user.healthfolder.id,
            "family_medical_history": user.healthfolder.family_medical_history
        } if user.healthfolder else None
    }

    return jsonify(user_data), 200
