from Recipe import Recipe


class DietaryRecipe(Recipe):
    def __init__(self, Title, Diet_type, Ingredients=None):
        super().__init__(Title, Ingredients)
        self.diet_type = Diet_type

    def scale(self, ratio: float):
        recipe = super().scale(ratio)
        dietaryRecipe0 = DietaryRecipe(recipe.title, self.diet_type, recipe.ingredients)
        return dietaryRecipe0

    def __str__(self):
        return f"[{self.diet_type}] " + super().__str__()


