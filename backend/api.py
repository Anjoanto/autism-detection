from flask import Flask, render_template, jsonify, request
import handTrack
import os
app = Flask(__name__)
cour = [
    {'a': '123', 'b': 'B'},
    {'a': '123', 'b': 'B'}
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/track')
def show():
    # exec(open('handTrack.py')
    try:
        os.remove('test.csv')
        os.remove('free.csv')
        os.remove('aut.png')
    except:
        print('error')

    return jsonify(handTrack.trackHand())

if __name__ == '__main__':
    app.run(debug=True)

