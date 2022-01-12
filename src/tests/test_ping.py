def test_ping(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/health")

    # Then
    assert response.status_code == 200
    assert response.json() == {
        "ping": "pong",
        "environment": "test",
        "testing": True,
        "database_url": "postgres://root:password@db:5432/test",
    }
