from app import db

class CampaignStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    action_type = db.Column(db.String(50))  # e.g., 'send_email', 'send_whatsapp', etc.
    action_data = db.Column(db.Text)  # JSON with action params
    trigger_time = db.Column(db.DateTime)  # When to trigger
    status = db.Column(db.String(20), default='pending')

    def __repr__(self):
        return f'<CampaignStep {self.action_type}>'
