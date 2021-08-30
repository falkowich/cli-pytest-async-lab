import pytest


def pytest_addoption(parser):
    parser.addoption("--switch", action="store")


@pytest.fixture(scope="session")
def switch(request):
    switch_value = request.config.option.switch
    if switch_value is None:
        pytest.skip()
    return switch_value
