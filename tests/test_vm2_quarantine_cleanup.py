import pytest

@pytest.fixture(scope="session", autouse=True)
def global_session_resource():
    print("VM2_SESSION_RESOURCE_SETUP_OK")
    yield
    print("VM2_SESSION_RESOURCE_TEARDOWN_OK")


def test_healthy_non_quarantined():
    print("VM2_HEALTHY_TEST_BODY_PASS")
    assert True


def test_quarantined_case():
    print("VM2_QUARANTINED_TEST_BODY_PASS")
    assert True
