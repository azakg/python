from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sandBox/FrontEnd_BackEnd_example/submit', methods=['POST'])
def submit():
    text_input = request.form.get('textInput')
    # Проверка, что текст был получен
    if text_input:
        print("Success")
        print(f"Received text: {text_input}")
    else:
        print("No text received")

    return f"Text received: {text_input}"

if __name__ == '__main__':
   app.run(port=5000, debug=True)