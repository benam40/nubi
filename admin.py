from app import app, db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from contacts.models import Contact
from campaigns.models import Campaign
from integrations.models import IntegrationConfig

admin = Admin(app, name='Nubi Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Contact, db.session))
admin.add_view(ModelView(Campaign, db.session))
admin.add_view(ModelView(IntegrationConfig, db.session))
