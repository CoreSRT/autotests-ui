import pytest


@pytest.mark.smoke
def test_smoke_case():
    pass


@pytest.mark.regression
def test_regression():
    pass


@pytest.mark.smoke
class TestSuite:
    def test_case1(self):
        pass

    def test_case2(self):
        pass


@pytest.mark.ui
class TestUserAuthentication:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    @pytest.mark.smoke
    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    pass
