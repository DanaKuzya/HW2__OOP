from Ingredient import Ingredient


class Recipe:
    def __init__(self, Title, Ingredients=None):
        self.title = Title
        self.ingredients = Ingredients

    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self.ingredients:
            if ingr == ingredient:
                ingr.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if type(ratio) == float or type(ratio) == int:
            if ratio > 0:
                return True
        return False

    def scale(self, ratio: float):
        recipe1 = Recipe(self.title)
        for ingr in self.ingredients:
            ingr1 = Ingredient(ingr.name, ingr.quantity * ratio, ingr.unit)
            recipe1.add_ingredient(ingr1)
        return recipe1

    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        list0 = ""
        for ingr in self.ingredients:
            list0 += str(ingr) + "\n"
        return list0




