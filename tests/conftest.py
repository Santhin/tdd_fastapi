
import pytest
from starlette.testclient import TestClient
from app import main
from app.config import get_settings, Settings, DATABASE_TEST_URL


def get_settings_override():
    return Settings(testing=True, database_url=DATABASE_TEST_URL)


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as client:
        yield client
    # Tear down