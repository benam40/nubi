from flask import Blueprint, request, jsonify
from .models import IntegrationConfig
from app import db

integrations_bp = Blueprint('integrations', __name__)

@integrations_bp.route('/integrations', methods=['GET'])
def list_integrations():
    configs = IntegrationConfig.query.all()
    return jsonify([
        {
            'id': c.id,
            'name': c.name,
            'api_key': c.api_key,
            'api_secret': c.api_secret,
            'access_token': c.access_token,
            'refresh_token': c.refresh_token,
            'extra': c.extra
        } for c in configs
    ])

@integrations_bp.route('/integrations', methods=['POST'])
def add_integration():
    data = request.json
    config = IntegrationConfig(
        name=data['name'],
        api_key=data.get('api_key'),
        api_secret=data.get('api_secret'),
        access_token=data.get('access_token'),
        refresh_token=data.get('refresh_token'),
        extra=data.get('extra')
    )
    db.session.add(config)
    db.session.commit()
    return jsonify({'id': config.id, 'name': config.name}), 201
