from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///local.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Import and register Blueprints
from contacts.routes import contacts_bp
from campaigns.routes import campaigns_bp
from integrations.telegram.routes import telegram_bp
from integrations.routes import integrations_bp
from integrations.whatsapp.routes import whatsapp_bp
from integrations.tiktok.routes import tiktok_bp
from integrations.calendar.routes import calendar_bp
from campaigns.automation import automation_bp
import admin  # Enables Flask-Admin dashboard

app.register_blueprint(contacts_bp)
app.register_blueprint(campaigns_bp)
app.register_blueprint(telegram_bp)
app.register_blueprint(integrations_bp)
app.register_blueprint(whatsapp_bp)
app.register_blueprint(tiktok_bp)
app.register_blueprint(calendar_bp)
app.register_blueprint(automation_bp)

@app.route('/')
def home():
    return 'Welcome to Nubi Marketing Automation Platform!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
