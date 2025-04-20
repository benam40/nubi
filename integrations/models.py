from app import db

class IntegrationConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    api_key = db.Column(db.String(255))
    api_secret = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    refresh_token = db.Column(db.String(255))
    extra = db.Column(db.Text)  # For JSON or additional config

    def __repr__(self):
        return f'<IntegrationConfig {self.name}>'
