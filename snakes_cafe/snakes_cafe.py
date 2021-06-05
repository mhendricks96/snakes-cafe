print("**************************************")
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print('** To quit at any time, type "quit" **')
print("**************************************")
print(" ")
print("Appetizers")
print("----------")
print("Wings")
print("Cookies")
print("Spring Rolls")
print(" ")
print("Entrees")
print("-------")
print("Salmon")
print("Steak")
print("Meat Tornado")
print("A Literal Garden")
print(" ")
print("Desserts")
print("--------")
print("Ice Cream")
print("Cake")
print("Pie")
print(" ")
print("Drinks")
print("------")
print("Coffee")
print("Tea")
print("Unicorn Tears")
print(" ")
print("***********************************")
print("** What would you like to order? **")
print("***********************************")


# Global Variables
chosen_items = {}

# Functions
def addChoice(choice):
  
  print(choice)
  if choice == "quit":
    print(f"Goodbye! Here is what you have in your meal {chosen_items}")
    quit()
  elif choice in chosen_items:
    chosen_items[choice] = chosen_items[choice] + 1
    print(f"{chosen_items[choice]} orders of {choice} has been added to your meal")
    askAgain()
  else:
    chosen_items[choice] = 1
    print(f"{chosen_items[choice]} order of {choice} has been added to your meal")
    askAgain()

def askAgain():
  userChoice = input("anything else? > ")
  addChoice(userChoice)   

#Executable Code
userChoice = input("> ")
addChoice(userChoice)






