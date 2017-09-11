from flask import request, jsonify, g
from application.models import Category
from index import app, db
from sqlalchemy.exc import IntegrityError
from application.utils import Http, requires_auth
from application.urls import Urls

def cat_helper(cat):
    return {
        'name': cat,
        'id': ++id
    }

@app.route(Urls.CATEGORIES, methods=[Http.GET])
def get_categories():
    cats = Category.query.all()
    return jsonify(result=[category.attr() for category in cats]), 200


@app.route(Urls.CATEGORIES, methods=[Http.POST])
@requires_auth
def create_category():
    incoming = request.get_json()
    data = incoming['data']
    category = Category(
        name=data['name'],
        description=data.get('description'),
        created_by=g.current_user['id']
    )
    db.session.add(category)
    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message='Category unable to be created'), 409

    return jsonify({}), 201

@app.route(Urls.CATEGORIES + '/<category_id>', methods=[Http.DELETE])
@requires_auth
def delete_category(category_id):

    category = Category.query.filter_by(
                    id=category_id
                ).first()

    if not category:
        return jsonify(message='Category not found'), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({}), 200
