# from flask import Flask

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, Guddiya!"

# if __name__ == "__main__":
#     app.run(debug= True)    

    # Create another page
    #  we can create multiple routes:

    
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"    

if __name__ == "__main__":
    app.run(debug=True)