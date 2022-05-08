import pickle
import items_class
import changePickle

items = pickle.load(open('main_items.p', 'rb'))

def searchIncredients(item):

    # Opens pickle and gets the incredients from it
    items = pickle.load(open('main_items.p', 'rb'))

    ingredients = item.ingredients_list()

    if ingredients != [None]:
        # Searches for the incredients in the pickle
        Item1 = items.get(ingredients[0])
        Item2 = items.get(ingredients[1])
    else:
        return 'No incredients'

    return Item1.name, Item2.name



try:

    print(searchIncredients(items.get(user_input))) # ToDo: add user_input input taker

except:
    # Considering the item was written correctly and no errors didn't occur
    print('Item not found')