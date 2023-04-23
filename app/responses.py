from flask import jsonify


def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200


def not_found():
    return jsonify({
        'success': False,
        'data': {},
        'status': 404,
        'message': 'Resource not found'
    }), 404
