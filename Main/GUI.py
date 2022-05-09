import pickle
import re
import easygui
import sys

items = pickle.load(open('main_items.p', 'rb'))

def getRecipies(item):
    items = pickle.load(open('main_items.p', 'rb'))
    toDo = []
    recipies = []
    toDo.append(item)

    while not toDo == []:
        toDo.remove(item)
        item1, item2 = searchIngcredients(items.get(item))
        item1, item2 = items.get(item1).name, items.get(item2).name

        toDo.append(item1)
        toDo.append(item2)
        
        recipie = '{} = {} and {} \n'.format(item, item1, item2)
        recipies.append(recipie)
        print(recipies)

        if searchIngcredients(items.get(item1)) == None:
            toDo.remove(item1)

        if searchIngcredients(items.get(item2)) == None:
            toDo.remove(item2)
        
        item = toDo[0]
        print(toDo)
        print(recipies)

    
    return recipies


def searchIngcredients(item):

    # Opens pickle and gets the ingredients from it
    items = pickle.load(open('main_items.p', 'rb'))

    ingredients = item.ingredients_list()

    if ingredients != [None]:
        # Searches for the ingredients in the pickle
        Item1 = items.get(ingredients[0])
        Item2 = items.get(ingredients[1])
    else:
        return None

    return Item1.name, Item2.name

def searchItems(item):

    try:

        return searchIgcredients(item)

    except:
        # Todo: add error message if try fails for other reason that 'Item not found'
        print('Item not found')

def main(GUI_Running):
    while GUI_Running:

        # Opens the GUI
        msg = 'Input item name'
        title = 'Search'
        fieldNames = ['Item name']
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        # Close the GUI if the user clicks cancel or X
        if fieldValues == None:
            sys.exit(0)


        # Get the item name and amount from fieldValues
        item = fieldValues[0].title()
        #baseAmount = int(fieldValues[1])

        # Search for the item
        if item in items:
            try:
                # Get the recipies
                recipies = getRecipies(item)
                # Print the recipies
                msg = recipies

            except:
                msg = 'Item found' + '\n' + 'There are no ingredients since in a basic item'
            
            title = item
            easygui.msgbox(msg, title)
        # If the item is not in the pickle or the user inputs an invalid item
        else:
            msg = 'Item {} not found'.format(item)
            title = 'Error'
            easygui.msgbox(msg, title)


main(GUI_Running=True)
