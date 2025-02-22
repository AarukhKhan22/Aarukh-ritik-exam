from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.getenv('USER') or os.getenv('USERNAME')
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput('top -bn1')

    return f"""
    <html>
    <body>
    <h1>Name: Your Full Name</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {current_time}</h2>
    <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
