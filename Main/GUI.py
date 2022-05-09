import pickle
import easygui

items = pickle.load(open('main_items.p', 'rb'))

def searchIgcredients(item):

    # Opens pickle and gets the ingredients from it
    items = pickle.load(open('main_items.p', 'rb'))

    ingredients = item.ingredients_list()

    if ingredients != [None]:
        # Searches for the ingredients in the pickle
        Item1 = items.get(ingredients[0])
        Item2 = items.get(ingredients[1])
    else:
        return 'No ingredients'

    return Item1.name, Item2.name

def searchItems(item):

    try:

        return searchIgcredients(item)

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

        item = fieldValues[0].title()

        if fieldValues == None:
            GUI_Running = False

        if item in items:
            try:
                item1, item2 = searchItems(items.get(item))
                msg = 'Item {} found'.format(item) + '\n' + 'The recipe is: {} and {}'.format(items.get(item1).name, items.get(item2).name)
            except:
                msg = 'Item found' + '\n' + 'There are no ingredients since in a basic item'

            GUI_Running = False
            
            title = item
            easygui.msgbox(msg, title)
        
        else:
            msg = 'Item {} not found'.format(item)
            title = 'Error'
            easygui.msgbox(msg, title)


main(GUI_Running=True)
