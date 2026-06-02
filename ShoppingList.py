from Ingredient import Ingredient

from Recipe import Recipe


class ShoppingList:
    def __init__(self, _Items):
        self._items = _Items

    def add_recipe(self, recipe: Recipe, portions: float):
        if not Recipe.is_valid_ratio(portions):
            raise ValueError ("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        for ingr in recipe.ingredients:
            self._items.append((ingr, recipe.title))

    def remove_recipe(self, title: str):
        items = []
        for item in self._items:
            if item[1] != title:
                items.append(item)
        self._items = items

    def get_list(self):
        list1 = dict()
        for item in self._items():
            if (item[0].name, item[0].unit) in list1:
                list1[(item[0].name, item[0].unit)] += item.quantity
            else:
                list1[(item[0].name, item[0].unit)] = item.quantity
        list0 = []
        for key, val in list1.items():
            ingr = Ingredient(key[0], val, key[1])
            list0.append(ingr)
        list0.sort(key=lambda x: x.name)
        return list0

    def __add__(self, other: ShoppingList):
        list0 = ShoppingList(self._items + other._items)
        return list0


