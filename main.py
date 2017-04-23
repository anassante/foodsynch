from flask import Flask, render_template, request
from jsonfilter import jsonFilter
import filterlist

app = Flask(__name__)


outputlist = None


@app.route('/')
@app.route('/<user>')
def index(user=None):
	return render_template("user.html", user=user)

@app.route('/home')
def home():
	return "this is home"
@app.route('/planingid/<int:planingid>', methods=['GET'])
def planing(planingid):
	return render_template("profile.html", planingid=planingid)

@app.route('/planingid/<int:planingid>', methods=['POST'])
def my_form_post(planingid):
	text = request.form['restrictions']

	processed_text = text
	print(processed_text)

	templist = processed_text.split()
	print(templist)

	recipelist = jsonFilter(templist)
	print(recipelist)



	retval = '<ol>'
	for item in recipelist:
		retval += '<li><a href="' + item[1] + '">' + item[0] + '</a></li>'

	retval += '</ol>'
	return retval












if __name__ == "__main__":
	app.run(debug=True)