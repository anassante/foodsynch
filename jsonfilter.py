import json

def isAcceptable(li, filter_ingredients):
  for i in li:
    if i in filter_ingredients:
      return False
  return True

def jsonFilter(listy):
	returnlist = []
	with open('openrecipes.json') as data_file:
		data = json.load(data_file)
	for i in range(30):
		data_lowered = data[i]['ingredients'].lower()
		#print("DEBUG DW",data_lowered)
		#print("DEBUG ELEMENT",element)
		if (isAcceptable(listy, data_lowered)):
			returnlist.append([data[i]['name'], data[i]['url']])



	return returnlist

#for element in data_loaded:
	#if (processed_text) in print(p['ingredients'])
