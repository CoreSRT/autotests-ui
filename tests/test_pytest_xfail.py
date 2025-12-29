import pytest


@pytest.mark.xfail(
    reason='Известный баг, будет исправлен'
)
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(
    reason='Баг исправлен, но все еще маркировка xfail'
)
def test_without_bug():
    pass


@pytest.mark.xfail(
    reason='Внешний сервис временно недоступен'
)
def test_external_services_is_unavailable():
    assert 1 == 2
