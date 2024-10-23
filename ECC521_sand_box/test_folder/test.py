from flask import Flask, render_template, request, redirect, jsonify
import json

test = Flask(__name__)

JF = 'fs.json'

@test.route('/')
def index():
    with open(JF, 'r') as f:
        feedback_data = json.load(f)
        return render_template('test.html', feedback=feedback_data)


@test.route('/click', method=['POST'])
def click():
    test_input = request.form['test_input']
    text_area = request.form['text_area']
    print(text_area)

