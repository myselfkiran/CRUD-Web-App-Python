# CRUD Web App using Flask
# Full Flask code will be added here soon.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "CRUD Web App - Coming Soon!"

if __name__ == "__main__":
    app.run(debug=True)
