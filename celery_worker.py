from celery import Celery
import os

celery = Celery(
    'nubi_app',
    broker=os.getenv('REDIS_URL', 'redis://localhost:6379/0'),
    backend=os.getenv('REDIS_URL', 'redis://localhost:6379/0')
)

@celery.task
def send_campaign_message(contact_id, campaign_id):
    # Placeholder: Implement actual campaign message sending logic
    print(f"Sending campaign {campaign_id} to contact {contact_id}")
    return True
