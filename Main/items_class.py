class Items:

    def __init__(self, name, farmability, ingredients):
        self.name = name
        self.farmability = farmability
        self.ingredients = ingredients
        
    
    def print_item(self):
        return self.name, self.farmability, self.ingredients

    def ingredients_list(self):
        return self.ingredients