import pytest
from data import test_buns


class TestBun:
    @pytest.mark.parametrize('bun', test_buns)
    def test_bun_get_name(self, bun):
        assert bun.get_name() == bun.name

    @pytest.mark.parametrize('bun', test_buns)
    def test_bun_get_price(self, bun):
        assert bun.get_price() == bun.price

