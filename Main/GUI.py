import pickle
import easygui
import sys

items = pickle.load(open('main_items.p', 'rb'))

def getRecipies(item, amount):
    items = pickle.load(open('main_items.p', 'rb'))
    toDo = []
    recipies = []
    amounts = []
    toDo.append(item)

    while not toDo == []:
        item1, item2 = searchIngredients(items.get(item))
        item1, item2 = items.get(item1).name, items.get(item2).name

        # Check if farmability of item is 0
        if items.get(item).farmability == 0:
            amount1, amount2 = amount*1.2, amount*1.2
        # Check if farmability of item is 1
        elif items.get(item).farmability == 1:
            amount1, amount2 = amount*0.8, amount*0.8
        else:
            print('Error')
        
        amounts.append(amount1)
        amounts.append(amount2)
        toDo.append(item1)
        toDo.append(item2)
        
        recipie = '{} ({}) = {} ({}) and {} ({})\n'.format(item, amount, item1, amount1, item2, amount2)
        recipies.append(recipie)

        if searchIngredients(items.get(item1)) == None:
            toDo.remove(item1)

        if searchIngredients(items.get(item2)) == None:
            toDo.remove(item2)
        
        amount = amounts[0]
        item = toDo[0]
        toDo.remove(item)

    return recipies


def searchIngredients(item):

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

        return searchIngredients(item)

    except:
        # Todo: add error message if try fails for other reason that 'Item not found'
        print('Item not found')

def main(GUI_Running):
    while GUI_Running:

        # Opens the GUI
        msg = 'Input item name'
        title = 'Search'
        fieldNames = ['Item name', 'Amount']
        fieldValues = []
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        # Close the GUI if the user clicks cancel or X
        if fieldValues == None:
            sys.exit(0)


        # Get the item name and amount from fieldValues
        item = fieldValues[0].title()
        amount = int(fieldValues[1])
        #baseAmount = int(fieldValues[1])

        # Search for the item
        if item in items:
            
            try:
                recipies = getRecipies(item, amount)
                # Print the recipies
                msg = recipies

            except:
                msg = 'Item is basic item'
            
            title = item
            easygui.msgbox(msg, title)
            
        # If the item is not in the pickle or the user inputs an invalid item
        else:
            msg = 'Item {} not found'.format(item)
            title = 'Error'
            easygui.msgbox(msg, title)


main(GUI_Running=True)
