from flask import Blueprint, request, jsonify

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar/create', methods=['POST'])
def create_event():
    # Placeholder: integrate with Google Calendar API
    data = request.json
    title = data['title']
    start = data['start']
    end = data['end']
    # create_calendar_event(title, start, end)
    return jsonify({'status': 'created', 'title': title, 'start': start, 'end': end})
