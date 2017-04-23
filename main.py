from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
@app.route('/<user>')
def index(user=None):
	return render_template("user.html", user=user)

@app.route('/home')
def home():
	return "this is home"
@app.route('/planingid/<int:planingid>', methods=['GET','POST'])
def planing(planingid):
	return render_template("profile.html", planingid=planingid)












if __name__ == "__main__":
	app.run(debug=True)