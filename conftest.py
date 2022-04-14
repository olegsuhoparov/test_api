from helpers.app import App
import pytest


@pytest.fixture
def app():
    return App()
