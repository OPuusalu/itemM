import pickle
import easygui

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

def searchItems(item):

    try:

        return searchIncredients(item)

    except:
        # Todo: add error message if try fails for other reason that 'Item not found'
        print('Item not found')

def main(GUI_Running):
    while GUI_Running:
        msg = 'Input item name'
        title = 'Search'
        fieldNames = ['Item name']
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        if fieldValues == None:
            GUI_Running = False

        if fieldValues[0] in items:
            item = fieldValues[0]
            item1, item2 = searchItems(items.get(item))
            GUI_Running = False
            msg = 'Item found' + '\n' + 'the recipe is: ' + items.get(item1).name + ' and ' + items.get(item2).name
            title = item
            easygui.msgbox(msg, title)
        
        else:
            msg = 'Item not found'
            title = 'Error'
            easygui.msgbox(msg, title)


main(GUI_Running=True)