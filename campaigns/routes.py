from flask import Blueprint, request, jsonify
from .models import Campaign
from app import db

campaigns_bp = Blueprint('campaigns', __name__)

@campaigns_bp.route('/campaigns', methods=['GET'])
def get_campaigns():
    campaigns = Campaign.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'type': c.type} for c in campaigns])

@campaigns_bp.route('/campaigns', methods=['POST'])
def add_campaign():
    data = request.json
    campaign = Campaign(name=data['name'], type=data.get('type'))
    db.session.add(campaign)
    db.session.commit()
    return jsonify({'id': campaign.id, 'name': campaign.name, 'type': campaign.type}), 201
