# IMPORTING THE NECESSARY MODULE NEEDED
from flask import Flask

# CREATING THE APP
app = Flask(__name__)


# HERE ROUTES ARE CREATED FOR THE APP
@app.route('/')   # CREATING THE PATH. GETS ADDED TO THE END OF THE LINK
def hello_world():    # DEFINING A FUNCTION WHICH CREATES THE HEADING/TEXT
    return "<body style=background-color:red><h1>This is my first Flask app</h1></body>"
# WHAT I WANT THE OUTCOME TO BE
# HERE THE HEADING SIZE IS SET
# AS WELL AS THE BACKGROUND COLOR


@app.route("/index/")
def index_page():
    return "<body style=background-color:orange><h1>This is my home page</h1></body>"


@app.route("/about/")
def about_page():
    return "<body style=background-color:yellow><h1>This is my about page</h1></body>"


@app.route("/projects/")
def projects_page():
    return "<body style=background-color:green><h1>This is my projects page</h1></body>"


@app.route("/contact/")
def contact_page():
    return "<body style=background-color:blue><h1>This is my contact page</h1></body>"


if __name__ == '__main__':
    app.debug = True
    app.run()
