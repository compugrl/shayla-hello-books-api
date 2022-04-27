
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def handle_books():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

# @books_bp.route("", methods=["GET"])
# def get_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return jsonify(books_response)
#
# @books_bp.route("/<book_id>", methods=["GET"])
# def get_one_book(book_id):
#     book = validate_book(book_id)
#
#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }
