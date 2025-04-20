from flask import Blueprint, request, jsonify
from .steps import CampaignStep
from app import db
from celery_worker import send_campaign_message

automation_bp = Blueprint('automation', __name__)

@automation_bp.route('/campaigns/<int:campaign_id>/trigger', methods=['POST'])
def trigger_campaign(campaign_id):
    # Example: trigger all steps for this campaign (in real scenario, filter by time/status)
    steps = CampaignStep.query.filter_by(campaign_id=campaign_id, status='pending').all()
    for step in steps:
        # For demo, just trigger a Celery job for each step
        send_campaign_message.delay(contact_id=1, campaign_id=campaign_id)  # Replace with actual contact logic
        step.status = 'sent'
    db.session.commit()
    return jsonify({'status': 'triggered', 'steps': len(steps)})
