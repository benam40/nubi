from flask import Blueprint, request, jsonify

tiktok_bp = Blueprint('tiktok', __name__)

@tiktok_bp.route('/tiktok/post', methods=['POST'])
def post_tiktok():
    # Placeholder: integrate with TikTok API
    data = request.json
    video_url = data['video_url']
    caption = data['caption']
    # post_tiktok_video(video_url, caption)
    return jsonify({'status': 'posted', 'video_url': video_url, 'caption': caption})
