from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        return "<h1>Welcome to home Page</h1>", 200
    except Exception as e:
        return f"An error occurred: {e}", 500
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)