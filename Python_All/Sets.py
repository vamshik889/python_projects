fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

  # Use the correct method to add multiple items (more_fruits) to the fruits set.
  #update function
  fruits = {"apple", "banana", "cherry"}
  more_fruits = ["orange", "mango", "grapes"]
  fruits.update(more_fruits)
print(fruits)