class Items:

    def __init__(self, name, farmability, ingredients, rarity):
        self.name = name
        self.farmability = farmability
        self.ingredients = ingredients
        self.rarity = rarity
        
    
    def print_item(self):
        return self.name, self.farmability, self.ingredients, self.rarity

    def ingredients_list(self):
        return self.ingredients
    
    # Return farmability of item
    def get_farmability(self):
        return self.farmability