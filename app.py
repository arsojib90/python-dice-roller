from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

dice_faces = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roll')
def roll_dice():
    face = random.choice(dice_faces)
    return jsonify({'face': face, 'number': dice_faces.index(face) + 1})

if __name__ == '__main__':
    app.run(debug=True)
