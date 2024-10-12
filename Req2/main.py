from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')
    return render_template('submit.html')
    
if __name__ == '__main__':
    app.run(debug=True)
