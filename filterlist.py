recipes = []
recipes.append(['eggs', 'flour', 'milk', 'sugar'])
recipes.append(['apples', 'cinnamon', 'honey', 'oats'])
recipes.append(['rice', 'seaweed', 'cucumbers', 'shoyu'])
recipes.append(['pasta', 'salt', 'tomato sauce', 'ground beef'])
recipes.append(['applesauce', 'flour', 'cocoa', 'sugar', 'oats'])

### vegan example

nonvegan = ['eggs', 'milk', 'ground beef', 'honey']

def isVegan(li):
  for i in li:
    if i in nonvegan:
      return False
  return True

filtered = [i for i in recipes if isVegan(i)]

# the previous list comprehension does the same thing as this for loop:
# for i in recipes:
#   if isVegan(i):
#     print(i)

#print(filtered)

### generalized version

#filter_ingredients = []

# response = input("Let's look at your first guest's food preferences. Is there anything they're unable to eat?")

# while True:
#   if response.lower() in ['n', 'no', 'nope', 'nothing']:
#     break
#   else:
#     filter_ingredients.append(response)
    
#   response = input("Is there anything else they're unable to eat?")
  
def isAcceptable(li):
  for i in li:
    if i in filter_ingredients:
      return False
  return True
def filterList(li):
  return [i for i in recipes if isAcceptable(i)]


