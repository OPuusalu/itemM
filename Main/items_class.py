class Items:

    def __init__(self, ID, name, farmability, incredients):
        self.ID = ID
        self.name = name
        self.farmability = farmability
        self.incredients = incredients
        
    
    def print_item(self):
        return self.ID, self.name, self.farmability, self.incredients

    def return_incredients(self):
        return self.incredients