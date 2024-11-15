from unittest.mock import Mock
import pytest
from data import (
    MOCK_BUN_PRICE,
    MOCK_BUN_NAME,
    MOCK_ING_NAME_1,
    MOCK_ING_TYPE_1,
    MOCK_ING_PRICE_1,
    MOCK_ING_TYPE_2,
    MOCK_ING_PRICE_2,
    MOCK_ING_NAME_2,
)


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_name.return_value = MOCK_BUN_NAME
    bun_mock.get_price.return_value = MOCK_BUN_PRICE
    return bun_mock


@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_name.return_value = MOCK_ING_NAME_1
    ingredient_mock.get_type.return_value = MOCK_ING_TYPE_1
    ingredient_mock.get_price.return_value = MOCK_ING_PRICE_1
    return ingredient_mock


@pytest.fixture
def two_ingredients_mock(ingredient_mock):
    ingredient_mock_2 = Mock()
    ingredient_mock_2.get_name.return_value = MOCK_ING_NAME_2
    ingredient_mock_2.get_price.return_value = MOCK_ING_PRICE_2
    ingredient_mock_2.get_type.return_value = MOCK_ING_TYPE_2
    ingredients_mock = [ingredient_mock, ingredient_mock_2]
    return ingredients_mock

