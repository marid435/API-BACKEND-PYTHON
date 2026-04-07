from src.app import create_app


def test_ping_status_code_is_200() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/ping")

    assert response.status_code == 200


def test_ping_response_body_is_pong() -> None:
    app = create_app()
    client = app.test_client()

    response = client.get("/ping")

    assert response.get_json() == {"message": "pong"}
