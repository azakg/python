from flask import Flask, render_template, request, redirect, jsonify
import json
import os

app = Flask(__name__)

# Path to the JSON file to store feedback
FEEDBACK_FILE = 'feedback.json'

# Ensure the feedback file exists
if not os.path.exists(FEEDBACK_FILE):
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump([], f)


# Route to render the main page with feedback form
@app.route('/')
def index():
    # Load feedback from the JSON file
    with open(FEEDBACK_FILE, 'r') as f:
        feedback_data = json.load(f)
    return render_template('index.html', feedback=feedback_data)


# Route to handle form submission
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    # Get the data from the form
    name = request.form['name']
    feedback = request.form['feedback']

    # Path to the JSON file
    feedback_file = 'feedback.json'

    # Load the existing feedback from the JSON file
    with open(feedback_file, 'r') as f:
        feedback_data = json.load(f)

    # Append new feedback to the data list
    feedback_data.append({
        'name': name,
        'feedback': feedback
    })

    # Write the updated feedback back to the JSON file
    with open(feedback_file, 'w') as f:
        json.dump(feedback_data, f, indent=4)

    # Redirect back to the homepage after saving
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
