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

chosen_items = {}

chosen_item = input ("> ")
chosen_items[chosen_item] = 1

print(f"{len(chosen_items)} order of {chosen_item} has been added to your meal")

print("Anything Else?")
second_choice = input("> ")

if second_choice == chosen_item:
  chosen_items[chosen_item] = 2
  print(f"2 orders of {chosen_item} has been added to your meal")
else:
  chosen_items[second_choice] = 1
  print(f"1 order of {second_choice} has been added to your meal")
