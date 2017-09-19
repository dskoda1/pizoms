from datetime import datetime

from flask import request, jsonify, g
from application.models import Size
from index import app, db
from sqlalchemy.exc import IntegrityError
from application.utils import Http, requires_auth
from application.urls import Urls

@app.route(Urls.SIZES, methods=[Http.GET])
def get_sizes():
    cats = Size.query.all()
    return jsonify(result=[size.attr() for size in sizes]), 200


@app.route(Urls.SIZES, methods=[Http.POST])
@requires_auth
def create_size():
    incoming = request.get_json()
    data = incoming['data']
    size = Size(
        size=data.get('size'),
        created_by=g.current_user['id']
    )
    db.session.add(size)
    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message='Size unable to be created'), 409

    return jsonify({}), 201

@app.route(Urls.SIZES + '/<size_id>', methods=[Http.DELETE])
@requires_auth
def delete_size(size_id):
    size = Size.query.filter_by(
                id=size_id
            ).first()

    if not size:
        return jsonify(message='Size not found'), 404

    db.session.delete(size)
    db.session.commit()
    return jsonify({}), 200
