from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def handle_submit():
    fname = request.form.get('fname', 'FNAME')
    lname = request.form.get('lname', 'LNAME')
    return render_template('result.html', first_name=fname, last_name=lname)

if __name__ == "__main__":
    app.run(host='0.0.0.0')