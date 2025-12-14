from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'GET':
            return jsonify({
                'success': True,
                "message": "GET request received"
            }), 200
        elif request.method == 'POST':
            data = request.get_json()
            if data is not None and 'name' in data:
                return jsonify({
                    'success': True,
                    "message": "POST request received",
                    "data": data
                }), 200
            else:
                return jsonify({
                    'success': False,
                    "message": "data parameter is missing or invalid"
                }), 400
    except Exception as e:
        if request.method =='GET':
            return jsonify({
                'success': False,
                "message": f"An error occurred during GET request: {str(e)}"
            }), 500
        elif request.method == 'POST':
            return jsonify({
                'success': False,
                "message": f"An error occurred during POST request: {str(e)}"
            }), 500
        
@app.route('/templates/<page>/<name>/<greetings>', methods=['GET'])
def templates(page, name, greetings):
    try:
        if request.method == 'GET':
            if name and greetings:
                my_list=['apple', 'banana', 'cherry', 'strawberry', 'watermelon']
                if page == 'home':
                    return render_template('index.html', page=page, name=name, greetings=greetings, my_list=my_list)
                elif page == 'other':
                    text = 'random text '
                    return render_template('other.html', page=page, name=name, greetings=greetings, my_list=my_list, text=text)
            else:
                return jsonify({
                    "success": False,
                    "message": "name or greetings parametere is missing"
                }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            "message": f"An error occurred while rendering template: {str(e)}"
        }), 500
    
@app.template_filter('reverse_string')
def reverse_string(string: str) -> str:
    return string[::-1]

@app.template_filter('repeat_string')
def repeat_string(string: str, times: int) -> str:
    return string * times

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)