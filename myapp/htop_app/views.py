import os
import subprocess
from datetime import datetime
from django.http import HttpResponse
import pytz

def htop_view(request):
    # Get system username
    username = os.getenv('USER') or os.getenv('USERNAME')

    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S IST')

    # Get top output
    top_output = subprocess.getoutput('top -bn1')

    response = f"""
    <html>
    <body>
    <h1>Name: Your Full Name</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {current_time}</h2>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response)
