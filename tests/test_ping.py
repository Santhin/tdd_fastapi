
def test_ping(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/health")
    
    # Then
    assert response.status_code == 200
    