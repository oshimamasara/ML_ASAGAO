from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/calc',methods=['POST'])
def calc():
    days = int(request.form['day'])
    url = 'http://localhost:5500/api'
    r = requests.post(url,json={'exp':days})
    x = round(r.json())
    return render_template('output.html',calc = x,day = days)
    

if __name__ == '__main__':
    app.run(port=5111,debug=True)