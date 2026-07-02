from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    return "Placement Tracker is running!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)