# app.py

from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting App</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(to right, #6a11cb, #2575fc);
                color: #fff;
                font-family: 'Arial', sans-serif;
                text-align: center;
                padding: 50px;
            }
            .container {
                max-width: 500px;
                margin: auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
            }
            input, button {
                width: 100%;
                margin: 10px 0;
            }
            button {
                background-color: #6a11cb;
                color: #fff;
            }
            button:hover {
                background-color: #2575fc;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to the Greeting App</h1>
            <p>Please enter your username to be greeted.</p>
            <form method="POST" action="/greet">
                <input class="form-control" type="text" name="username" placeholder="Enter your username" required>
                <button class="btn btn-primary" type="submit">Greet Me!</button>
            </form>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    username = request.form['username']
    # Introduce the vulnerability
    try:
        output = subprocess.check_output(f"echo Hello, {username}!", shell=True)
    except subprocess.CalledProcessError as e:
        output = str(e)
    
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Greeting App</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                background: linear-gradient(to right, #6a11cb, #2575fc);
                color: #fff;
                font-family: 'Arial', sans-serif;
                text-align: center;
                padding: 50px;
            }}
            .container {{
                max-width: 500px;
                margin: auto;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 10px;
            }}
            h2 {{
                margin-top: 20px;
            }}
            a {{
                color: #fff;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Greeting App</h1>
            <h2>{output}</h2>
            <a href="/">Go Back</a>
        </div>
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
