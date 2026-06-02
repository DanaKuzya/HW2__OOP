import pytest
from Ingredient import Ingredient
from ShoppingList import ShoppingList
from Recipe import Recipe


def test_ingredient_init():
    ingr = Ingredient("Молоко", 300.0, "мл")

    assert ingr.name == "Молоко"
    assert ingr.quantity == 300.0
    assert ingr.unit == "мл"

def test_ingredient_str():
    ingr = Ingredient("Яйцо", 2, "шт")

    assert str(ingr) == "Яйцо: 2 шт"

def test_ingredient_eq_1():
    firstIngr = Ingredient("Помидор", 1, "шт")
    secondIngr = Ingredient("Помидор", 2, "шт")

    assert (firstIngr == secondIngr) is True

def test_ingredient_eq_2():
    firstIngr = Ingredient("Помидор", 2, "шт")
    secondIngr = Ingredient("Огурец", 2, "шт")

    assert (firstIngr == secondIngr) is False

def test_ingredient_eq_3():
    firstIngr = Ingredient("Молоко", 500, "г")
    secondIngr = Ingredient("Молоко", 500, "мл")

    assert (firstIngr == secondIngr) is False

def test_recipe_init():
    recipe = Recipe("Название", [Ingredient("ingr1", 1, "шт"),
                                 Ingredient("ingr2", 1, "шт")])

    assert recipe.title == "Название"
    assert recipe.ingredients == [Ingredient("ingr1", 1, "шт"),
                                  Ingredient("ingr2", 1, "шт")]

def test_recipe_add_ingredient():
    recipe = Recipe("Название", [Ingredient("ingr1", 1, "шт"),
                                 Ingredient("ingr2", 1, "шт")])
    recipe.add_ingredient(Ingredient("ingr3", 1, "шт"))

    assert recipe.ingredients == [Ingredient("ingr1", 1, "шт"),
                                  Ingredient("ingr2", 1, "шт"),
                                  Ingredient("ingr3", 1, "шт")]

    recipe.add_ingredient(Ingredient("ingr3", 2, "шт"))

    assert recipe.ingredients == [Ingredient("ingr1", 1, "шт"),
                                  Ingredient("ingr2", 1, "шт"),
                                  Ingredient("ingr3", 3, "шт")]

def test_recipe_scale():
    recipe = Recipe("Название", [Ingredient("ingr1", 1, "шт"),
                                 Ingredient("ingr2", 1, "шт")])

    recipe1 = recipe.scale(2)

    assert recipe.ingredients == [Ingredient("ingr1", 1, "шт"),
                                  Ingredient("ingr2", 1, "шт")]
    assert recipe.title == "Название"
    assert recipe1.title == "Название"
    assert recipe1.ingredients == [Ingredient("ingr1", 2, "шт"),
                                   Ingredient("ingr2", 2, "шт")]

    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_recipe_len():
    recipe = Recipe("Название", [Ingredient("ingr1", 1, "шт"),
                                 Ingredient("ingr2", 1, "шт")])

    assert len(recipe) == 2

def test_shoppingList_add_recipe():
    recipe1 = Recipe("Блины", [Ingredient("Молоко", 200.0, "мл"),
                                 Ingredient("Яйцо", 2, "шт"),
                                 Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт")])
    sl = ShoppingList([(Ingredient("Молоко", 200.0, "мл"), recipe1.title)])
    sl.add_recipe(recipe2, 2)

    assert sl._items == [(Ingredient("Молоко", 200.0, "мл"), recipe1.title),
                         (Ingredient("Молоко", 400.0, "мл"), recipe2.title),
                         (Ingredient("Яйцо", 4, "шт"), recipe2.title)]
    with pytest.raises(ValueError):
        sl.add_recipe(recipe2, -1)

def test_shoppingList_remove_recipe():
    recipe1 = Recipe("Блины", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт"),
                               Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт")])
    sl = ShoppingList([(Ingredient("Молоко", 200.0, "мл"), recipe1.title)])
    sl.add_recipe(recipe2, 2)
    sl.remove_recipe(recipe1.title)

    assert sl._items == [(Ingredient("Молоко", 400.0, "мл"), recipe2.title),
                         (Ingredient("Яйцо", 4, "шт"), recipe2.title)]

    recipe3 = Recipe("Лазанья", [Ingredient("Макароны", 200.0, "г"),
                               Ingredient("Помидор", 2, "шт")])
    sl.remove_recipe(recipe3.title)

    assert sl._items == [(Ingredient("Молоко", 400.0, "мл"), recipe2.title),
                         (Ingredient("Яйцо", 4, "шт"), recipe2.title)]

def test_shoppingList_get_list():
    recipe1 = Recipe("Блины", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт"),
                               Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт")])
    recipe3 = Recipe("Лазанья", [Ingredient("Макароны", 200.0, "г"),
                                 Ingredient("Помидор", 2, "шт")])
    sl = ShoppingList([(Ingredient("Помидор", 2, "шт"), recipe3.title)])
    sl.add_recipe(recipe2, 2)
    sl.add_recipe(recipe1, 1)

    list0 = sl.get_list()

    assert list0 == [Ingredient("Молоко", 600.0, "мл"),
                     Ingredient("Мука", 200.0, "г"),
                     Ingredient("Помидор", 2, "шт"),
                     Ingredient("Яйцо", 6, "шт")]

def test_shoppingList_add():
    recipe1 = Recipe("Блины", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт"),
                               Ingredient("Мука", 200.0, "г")])
    recipe2 = Recipe("Омлет", [Ingredient("Молоко", 200.0, "мл"),
                               Ingredient("Яйцо", 2, "шт")])
    sl1 = ShoppingList([(Ingredient("Молоко", 200.0, "мл"), recipe1.title)])
    sl2 = ShoppingList([(Ingredient("Молоко", 200.0, "мл"), recipe2.title)])
    sl3 = sl1 + sl2

    assert sl1._items == [(Ingredient("Молоко", 200.0, "мл"), recipe1.title)]
    assert sl2._items == [(Ingredient("Молоко", 200.0, "мл"), recipe2.title)]
    assert sl3._items == [(Ingredient("Молоко", 200.0, "мл"), recipe1.title),
                          (Ingredient("Молоко", 200.0, "мл"), recipe2.title)]