import pickle

class Item:

    def addToPickle(item):
        
        # Opens the pickle if it exists, if not it creates a new one
        try:
            items = pickle.load(open('main_items.p', 'rb'))
        except:
            items = {} # can change this to add any other pickle to current one
            pickle.dump(items, open('main_items.p', 'wb'))

        items[item.name] = item

        pickle.dump(items, open('main_items.p', 'wb'))
    
    def removeFromPickle(item):
        # Opens the pickle if it exists else prints error
        try:
            items = pickle.load(open('main_items.p', 'rb'))

            items.pop(item.name)

            pickle.dump(items, open('main_items.p', 'wb'))

        except:
            print('Pickle not found')
    
    def renameItem(item, newName):
        # Opens the pickle if it exists else prints error
        try:
            items = pickle.load(open('main_items.p', 'rb'))

            # Renames the item in the pickle
            items[newName] = items.pop(item.name)

            pickle.dump(items, open('main_items.p', 'wb'))

        except:
            print('Pickle not found')
    
    def printItems():
        # Opens the pickle if it exists else prints error
        try:
            items = pickle.load(open('main_items.p', 'rb'))

            # Prints all the items in the pickle
            for item in items:
                print(item, items[item].print_item())

        except:
            print('Pickle not found')
            