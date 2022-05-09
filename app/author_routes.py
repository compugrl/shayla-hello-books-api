# Routes for authors
from os import abort
from app import db
from app.models.book import Book
from app.models.author import Author
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

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
    new_author = Author(author_name=request_body["author_name"])

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"author {new_author.author_name} successfully created"), 201)

@authors_bp.route("", methods=["GET"])
def read_all_authors():
    name_param = request.args.get("author_name")

    if name_param:
        authors = author.query.filter_by(author_name=name_param)
    else:
        authors = author.query.all()

    authors_response = []

    for author in authors:
        authors_response.append(
            {
                "author_id": author.id,
                "author_name": author.name
            }
        )
    return jsonify(authors_response)

@authors_bp.route("/<author_id>", methods=["GET"])
def read_one_author(author_id):
    author = validate_author(author_id)
    return {
            "author_id": author.id,
            "author_name": author.name
        }

@authors_bp.route("/<author_id>", methods=["PUT"])
def update_author(author_id):
    author = validate_author(author_id)

    request_body = request.get_json()

    author.name = request_body["author_name"]

    db.session.commit()

    return make_response(jsonify(f"author #{author.id} successfully updated"))

@authors_bp.route("/<author_id>", methods=["DELETE"])
def delete_author(author_id):
    author = validate_author(author_id)

    db.session.delete(author)
    db.session.commit()

    return make_response(jsonify(f"author #{author.id} successfully deleted"))