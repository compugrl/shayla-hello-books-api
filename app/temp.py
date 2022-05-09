
from os import abort
from app import db
from app.models.author import author
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")
author_bp = Blueprint("author_bp", __name__, url_prefix="/authors")

def validate_author(author_id):
    try:
        author_id = int(author_id)
    except:
        abort(make_response({"message":f"author {author_id} invalid"}, 400))

    author = author.query.get(author_id)

    if not author:
        abort(make_response({"message":f"author {author_id} not found"}, 404))

    return author

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = author(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"author {new_author.title} successfully created"), 201)

@authors_bp.route("", methods=["GET"])
def read_all_authors():
    
    title_query = request.args.get("title")
    if title_query:
        authors = author.query.filter_by(title=title_query)
    else:
        authors = author.query.all()

    authors_response = []
    for author in authors:
        authors_response.append(
            {
                "id": author.id,
                "title": author.title,
                "description": author.description
            }
        )
    return jsonify(authors_response)

@authors_bp.route("/<author_id>", methods=["GET"])
def read_one_author(author_id):
    author = validate_author(author_id)
    return {
            "id": author.id,
            "title": author.title,
            "description": author.description
        }

@authors_bp.route("/<author_id>", methods=["PUT"])
def update_author(author_id):
    author = validate_author(author_id)

    request_body = request.get_json()

    author.title = request_body["title"]
    author.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"author #{author.id} successfully updated"))

@authors_bp.route("/<author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = validate_author(author_id)

    db.session.delete(author)
    db.session.commit()

    return make_response(jsonify(f"author #{author.id} successfully deleted"))



