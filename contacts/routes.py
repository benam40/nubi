from flask import Blueprint, request, jsonify
from .models import Contact
from app import db

contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in contacts])

@contacts_bp.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    contact = Contact(name=data['name'], email=data['email'], phone=data.get('phone'))
    db.session.add(contact)
    db.session.commit()
    return jsonify({'id': contact.id, 'name': contact.name, 'email': contact.email, 'phone': contact.phone}), 201
