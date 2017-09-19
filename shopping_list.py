# make a list to hold onto our items
shopping_list = []

def show_help():
  
  # print out instructions on how to use the app
  print("what should we pick up at the store?")
  print("""
  Enter 'DONE' to stop adding items.
  Enter 'HELP' for this help.
  Enter 'SHOW' to see your current list.
  """)

def show_list():
    # print out the list
    print("Here is your list: ")
    
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
  
show_help()

# ask for new items
while True:
    new_item = input("> ")
    
 # be able to quit the app   
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
        
# add new items to our list
shopping_list.append(new_item)

show_list()