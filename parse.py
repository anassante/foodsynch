import json

with open('test.json') as json_file:  
    data = json.load(json_file)
    for p in data:
        print('Name: ' + p['name'])
        print('Website: ' + p['ingredients'])
        print('From: ' + p['recipeYield'])
        print('')
