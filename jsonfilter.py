import json

def jsonFilter(list):
	returnlist = []
	with open('test.json') as data_file:
		data = json.load(data_file)
	for i in range(50):
		data_lowered = data[i]['ingredients'].lower()
		for element in list:
			if (element  in data[i]['ingredients']):
				break
		returnlist.append([data[i]['name'], data[i]['url']])

	return returnlist

#for element in data_loaded:
	#if (processed_text) in print(p['ingredients'])
