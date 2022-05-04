def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "New Book",
        "description": "The Best!"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Book New Book successfully created"

def test_get_nonexisting_book(client, two_saved_books):
    # Act
    response = client.get("/books/12345698225498")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Book 12345698225498 not found"
    }

def test_get_invalid_book(client, two_saved_books):
    # Act
    response = client.get("/books/dog")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "message": "Book dog is invalid"
    }