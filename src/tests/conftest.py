import pytest
from starlette.testclient import TestClient

from app import main
from app.config import DATABASE_URL_TEST, Settings, get_settings


def get_settings_override():
    return Settings(environment="test", testing=True, database_url=DATABASE_URL_TEST)


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as client:
        yield client
    # Tear down
