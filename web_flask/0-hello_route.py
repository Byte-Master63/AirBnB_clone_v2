from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define the route /airbnb-onepage/ and its corresponding view function
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Run the Flask application on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
