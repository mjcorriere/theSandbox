from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Welcome to the index.'

@app.route('/hworld')
def hello_world():
	return 'Hello world, again'

@app.route('/users/<username>')
def display_user_profile(username):
	return 'User {0} has logged in!'.format(username)

@app.route('/post/<int:post_id>')
def display_post(post_id):
	return 'Blog post #{0}'.format(post_id)

if __name__ == '__main__':
	app.debug = True
	app.run()