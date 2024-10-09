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

@api_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Met à jour les informations de l'utilisateur spécifiées dans la requête.
    """
    user = User.query.get(user_id)
    
    if not user:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    # Récupérer les données de la requête JSON
    data = request.get_json()

    # Mettre à jour les champs spécifiés
    if "firstname" in data:
        user.firstname = data["firstname"]
    if "lastname" in data:
        user.lastname = data["lastname"]
    if "password" in data:
        user.password = data["password"]
    if "birth_date" in data:
        user.birth_date = data["birth_date"]
    if "weight" in data:
        user.weight = data["weight"]
    if "height" in data:
        user.height = data["height"]
    if "gender" in data:
        user.gender = data["gender"]
    if "digital_print" in data:
        user.digitalprint = data["digital_print"]
    if "eye_color" in data:
        user.eye_color = data["eye_color"]
    if "photo_identity" in data:
        user.photo_identity = data["photo_identity"]
    if "id_address" in data:
        user.id_address = data["id_address"]
    if "mutual_name" in data:
        user.mutual_name = data["mutual_name"]
    if "social_security_number" in data:
        user.social_security_number = data["social_security_number"]
    if "additional_infos" in data:
        user.additional_infos = data["additional_infos"]

    # Sauvegarder les modifications dans la base de données
    try:
        db.session.commit()
        return jsonify({"message": "Utilisateur mis à jour avec succès"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500