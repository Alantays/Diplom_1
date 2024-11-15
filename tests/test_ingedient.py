import pytest
from data import test_ingredients


class TestIngredient:
    @pytest.mark.parametrize('ingredient', test_ingredients)
    def test_ingredient_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient.name

    @pytest.mark.parametrize('ingredient', test_ingredients)
    def test_ingredient_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient.type

    @pytest.mark.parametrize('ingredient', test_ingredients)
    def test_ingredient_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient.price
