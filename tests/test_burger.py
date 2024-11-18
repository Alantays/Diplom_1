from praktikum.burger import Burger
from data import expected_receipt


class TestBurger:
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, bun_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        assert ingredient_mock in burger.ingredients

    def test_remove_ingredient(self, ingredient_mock):
        burger = Burger()
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert ingredient_mock not in burger.ingredients

    def test_move_ingredient(self, two_ingredients_mock):
        burger = Burger()
        ingredient_one, ingredient_two = two_ingredients_mock
        burger.add_ingredient(ingredient_one)
        burger.add_ingredient(ingredient_two)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == ingredient_two

    def test_get_price(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_price = bun_mock.get_price() * 2 + ingredient_mock.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt(self, bun_mock, ingredient_mock):
        burger = Burger()
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        receipt = burger.get_receipt()
        assert receipt == expected_receipt
