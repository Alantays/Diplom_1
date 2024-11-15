from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
#Buns
test_buns = [
    Bun('black bun', 100),
    Bun('white bun', 200),
    Bun('red bun', 300)
]

#Ingredients
test_ingredients = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
]

#Mock data
MOCK_BUN_NAME = 'black bun'
MOCK_BUN_PRICE = 100

MOCK_ING_TYPE_1 = 'SAUCE'
MOCK_ING_NAME_1 = 'hot sauce'
MOCK_ING_PRICE_1 = 100

MOCK_ING_TYPE_2 = 'FILLING'
MOCK_ING_NAME_2 = 'cutlet'
MOCK_ING_PRICE_2 = 100

expected_receipt = (
    f'(==== black bun ====)\n'
    f'= sauce hot sauce =\n'
    f'(==== black bun ====)\n\n'
    f'Price: 300'
)
