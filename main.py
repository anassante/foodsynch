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
@app.route('/planningid/<int:planningid>', methods=['GET'])
def planning(planningid):
	return render_template("profile.html", planningid=planningid)

@app.route('/planningid/<int:planningid>', methods=['POST'])
def my_form_post(planningid):
	text = request.form['restrictions']

	processed_text = text
	print(processed_text)

	templist = processed_text.split()
	print(templist)

	recipelist = jsonFilter(templist)
	print(recipelist)



	retval = '<h1>Here are your personalized recipes!</h1><br><ol>'
	for item in recipelist:
		retval += '<li><a href="' + item[1] + '">' + item[0] + '</a></li>'

	retval += '</ol>'
	return retval












if __name__ == "__main__":
	app.run(debug=True)