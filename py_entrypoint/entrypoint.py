#!/usr/bin/env python3
from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

# Function to get the host IP address
def get_host_ip():
    try:
        # Use socket to get the IP address of the host
        host_ip = socket.gethostbyname(socket.gethostname())
        
        # Read the content of the installed tools file
        with open('/workspace/installed_tools_readme.log', 'r') as file:
            installed_tools = file.read()

        return "Host IP Address: <br>" + host_ip + "<br>Installed tools:<br>" + installed_tools.replace('\n', '<br>')


    except Exception as e:
        return f"Error getting host IP address or reading installed tools file: {str(e)}"

# Display a welcome message, information about installed tools, and host IP address
@app.route('/')
def hello():
    try:
        response_text = get_host_ip()
        return response_text
    except Exception as e:
        return f"Error processing request: {str(e)}"

# Execute commands and display the result
@app.route('/cmd', methods=['POST'])
def execute_command():
    command = request.form.get('cmd', '')
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
        logs = f"Command executed successfully:\n{result}"
    except subprocess.CalledProcessError as e:
        logs = f"Error executing command:\n{e.output}"

    html = f"<html><body>Hi thre, good to see you <br/><br/>Logs:<br/><pre>{logs}</pre></body></html>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)