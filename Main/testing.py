import pickle
import items_class
import changePickle


Wooden_Platform = items_class.Items('Wooden Platform', 1, ['Wood Block', 'Grass'])

changePickle.Item.addToPickle(Wooden_Platform)
