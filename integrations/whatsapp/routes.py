from flask import Blueprint, request, jsonify

whatsapp_bp = Blueprint('whatsapp', __name__)

@whatsapp_bp.route('/whatsapp/send', methods=['POST'])
def send_whatsapp():
    # Placeholder: integrate with WhatsApp API (e.g., Twilio, WhatsApp Business API)
    data = request.json
    phone = data['phone']
    message = data['message']
    # send_whatsapp_message(phone, message)
    return jsonify({'status': 'sent', 'phone': phone, 'message': message})
