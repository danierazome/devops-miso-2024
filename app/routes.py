from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from models import Blacklist, db
from datetime import datetime

blacklist_bp = Blueprint('blacklists', __name__)

@blacklist_bp.route('/blacklists', methods=['POST'])
def create_blacklist_entry():
    data = request.get_json()
    ip_address = request.remote_addr
    new_entry = Blacklist(email=data.get('email'), created_at=datetime.utcnow(), ip=request.remote_addr,app_uuid=data.get('app_uuid'),blocked_reason=data.get('blocked_reason'))
    try:
        db.session.add(new_entry)
        db.session.commit()
    except IntegrityError as e:
        return jsonify({'error': str(e)}), 400
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
        
    return jsonify({'message': 'Blacklist entry created successfully'}), 201

@blacklist_bp.route('/blacklists/<string:email>', methods=['GET'])
def get_blacklis(email):
    entry = Blacklist.query.filter_by(email=email).first()
    response = {
        'is_blacklisted': False
    }

    if entry:
        response = {
        'is_blacklisted': True
        }
        if entry.blocked_reason:
            response['blocked_reason'] = entry.blocked_reason

    return jsonify(response), 200
