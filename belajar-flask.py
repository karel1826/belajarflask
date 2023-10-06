from flask import Flask, send_file, render_template
import os

app = Flask(__name__)

@app.route('/')
def indexRoute():
    return render_template('oke.html')
import json
@app.route('/json')
def jsonRoute(): 
    datajson = {
        'name': 'karel',
        'lastname': 'paterlini'
    }
    return json.dumps(datajson) 
@app.route('/img')
def img():
    return send_file('D:/py/static/mm1.jpg', as_attachment=True)

    
if __name__ == '__main__': 
    app.run('0.0.0.0' , debug=True)
    