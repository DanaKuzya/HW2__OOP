class Ingredient:
    def __init__(self, Name, Quantity, Unit):
        self.name = Name
        self.quantity = Quantity
        self.unit = Unit

    @property
    def quantity(self):
        return self.quantity

    @property.setter
    def quantity(self, quan):
        if quan <= 0:
            raise ValueError("Количество должно быть положительным")
        self.quantity = float(quan)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    def __eq__(self, other):
        if isinstance(other, Ingredient):
            if self.name == other.name and self.unit == other.unit:
                return True
        return False