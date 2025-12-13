from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return "<h1>Hello, world!</h1>"
    except Exception as e:
        return f"An error occured: {str(e)}", 500
    
@app.route('/hello')
def hello():
    try:
        return "hello world"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# url processor 
@app.route('/greet/<name>')
def greet(name):
    try:
        return f"Hello, {name}"
    except Exception as e:
        return f"AN error occured: {str(e)}", 500
    
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    try:
        return f"The sum is: {num1 + num2}"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
@app.route('/handle_url_params', methods=['GET', 'POST'])
def handle_url_params():
    try:
        if 'greeting' in request.args and 'name' in request.args:
            greeting = request.args['greeting']
            name = request.args['name']
            return f"<h1>hello, {name}, welcome to {greeting}!</h1>"
        else:
            return "<h1> some parameters are missing </h1>"
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
# request type handling
@app.route('/handle_request', methods=['GET', 'POST'])
def handle_request():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if data and 'name' in data:
                return {
                    "success": True,
                    "message": "POST request received",
                    "data": data
                }, 200
            else:
                return {
                    "success": False,
                    "message": "No JSON data provided in POST request"
                }, 400
        elif request.method == 'GET':
            return {
                "success": True,
                "message": "GET request received"
            }, 200

    except Exception as e:
        if request.method == 'POST':
            return {
                "success": False,
                "message": f"An error occured during POST request: {str(e)}"
            }, 500
        elif request.method == 'GET':
            return {
                "success": False,
                "message": f"An error occurred during GET request: {str(e)}"
            }, 500
        
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
