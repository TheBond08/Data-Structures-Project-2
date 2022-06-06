from lib.trees import trees
from lib.bst import binary_search_tree

while True:
    print("""
        1- binary search tree
        2- trees""")
    user_input = int(input("give me 1 or 2 or out of range to quit: "))
    if user_input == 1:
        binary_search_tree()
    elif user_input == 2:
        trees()
    else:
        break