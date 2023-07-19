from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/' , methods=['GET' , 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html', error_msg="")
	inputed_username = request.form['username']  
	inputed_pass = request.form['password']
	if (inputed_pass == password and username == inputed_username):
		return redirect(url_for('home'))
		
	return render_template('login.html' , error_msg="INCORRECT PASSWORD OR USERNAME")


@app.route('/home')
def home():
	return render_template('home.html' , friends_list=facebook_friends)

@app.route('/friend_exists/<string:name>' , methods=['GET' , 'POST'])
def friends(name):
	if request.method == 'GET':
		if name in facebook_friends:
			return render_template('friend_exists.html' , doexist = True)
		return render_template('friend_exists.html' , doexist = False)







if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)