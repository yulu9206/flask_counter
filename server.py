from flask import Flask, render_template, session  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
app.secret_key = 'ThisIsSecret'                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index(): 
	if 'num' in session:
		session['num'] += 1
	else:
		session['num'] = 0  	
  	return render_template('index.html')  # Return 'Hello World!' to the response.

@app.route('/add_two')
def addTwo():
	session['num'] += 2
	return render_template('index.html')

@app.route('/reset')
def reset():
	session['num'] = 1
	print session['num']
	return render_template('index.html')	

app.run(debug=True)