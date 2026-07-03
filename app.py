from flask import Flask , render_template

# Create an instance of the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    return render_template("home.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)