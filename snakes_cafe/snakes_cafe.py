print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print('** To quit at any time, type "quit" **')
print("**************************************")
print(
  '''
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    '''
)
print("***********************************")
print("** What would you like to order? **")
print("***********************************")




# Global Variables
chosen_items = {}
menu_options = ("Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Crea","Cake","Pie","Coffee","Tea","Unicorn Tears",) 

# Functions
def addChoice(choice):
  
  #print(choice)
  if choice == "Quit":
    print("Items added to list:")
    print('\n'.join("{}: {}".format(k, v) for k, v in chosen_items.items()))
    quit()
  elif choice in chosen_items and menu_options:
    chosen_items[choice] = chosen_items[choice] + 1
    print(f"{chosen_items[choice]} orders of {choice} has been added to your meal")
    askAgain()
  elif choice in menu_options:
    chosen_items[choice] = 1
    print(f"{chosen_items[choice]} order of {choice} has been added to your meal")
    askAgain()
  else:
    print("sorry, please choose something on the menu")

def askAgain():
  userInput = input("anything else? > ")
  userChoice = userInput.capitalize()
  addChoice(userChoice)
  askAgain()   

#Executable Code
userInput = input("> ")
userChoice = userInput.capitalize()
if userChoice in menu_options:
  addChoice(userChoice)
else:
  print("sorry, please something on the menu")
  askAgain()






