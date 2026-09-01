# from flask import Flask

# app = Flask(__name__)
# @app.route("/")
# def home():
#     return "Hello, Guddiya!"

# if __name__ == "__main__":
#     app.run(debug= True)    

    # Create another page
    #  we can create multiple routes:

import pandas as pd   
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

    df = pd.DataFram({
    "Name":["Guddiya","Aman","Riya"],
    "Marks":[90,85,95]
})

@app.route("/students")
def students():
    return df.to_html(index=False)
  

if __name__ == "__main__":
    app.run(debug=True)





# Flask + Pandas
# This is where Flask becomes particularly interesting for your
# Data Analysis learning.

# import pandas as pd
# from flask import Flask

# app = Flask(__name__)

# df = Flask(__name__)

# df = pd.DataFram({
#     "Name":["Guddiya","Aman","Riya"],
#     "Marks":[90,85,95]
# })

# @app.route("/students")
# def students():
#     return df.to_html(index=False)

# if __name__ == "__main__":
#     app.run(debug=True)    


  