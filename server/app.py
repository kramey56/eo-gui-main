from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from string import printable
import serial
import socket

# configuration
DEBUG=True
HOST = '192.168.18.65'
PORT = 8888

# instance the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def despace(s: str) -> str:
    """ Strip spaces from input string """
    return s.replace(b' ', b'').replace(b'(', b'').replace(b')', b'')

# A lambda function to strip spaces - testing to see which one more reliable
stripped = lambda s: b''.join(i for i in s if 31 < ord(i) < 127)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    """ Just tests that the server is awake """
    return jsonify('Hi, Ken!')

@app.route('/home', methods=['GET'])
def home_focuser():
    """ Return focuser to its home position - defined as the last commanded position """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'HOME')
    except (ConnectionRefusedError, ConnectionResetError):
        retval = 'HiRACS not responding'
    except Exception as e:
        retval = 'Unknown error occured'
        print(f'Error: {e}')
    else:
        retval = 'Focuser Homing'
    return jsonify(retval)

@app.route('/center', methods=['GET'])
def center_focuser():
    """ Move focuser to the middle of its travel range """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'CENTER')
    except (ConnectionRefusedError, ConnectionResetError):
        retval = 'HiRACS not responding'
    except Exception as e:
        retval = 'Unknown error occured'
        print(f'Error: {e}')
    else:
        retval = 'Focuser Centering'
    return jsonify(retval)

@app.route('/zero', methods=['GET'])
def zero_focuser():
    """ Set focuser to its zero point, which is completely retracted """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'MA000000')
    except (ConnectionRefusedError, ConnectionResetError):
        retval = 'HiRACS not responding'
    except Exception as e:
        retval = 'Unknown error occured'
        print(f'Error: {e}')
    else:
        retval = 'Focuser Bottoming'
    return jsonify(retval)

@app.route('/move', methods=['POST'])
def move_focuser():
    """ Move focuser to arbitrary position passed in as parameter to API call """
    target = str(request.form['target'])
    while len(target) < 6:
        target = '0' + target
    cmd = b'<F1MA' + target.encode() + b'>'
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(cmd)
    except (ConnectionRefusedError, ConnectionResetError):
        retval = 'HiRACS not responding'
    except Exception as e:
        retval = 'Unknown error occured'
        print(f'Error: {e}')
    else:
        retval = 'Focuser moving'
    return jsonify(retval)

@app.route('/status', methods=['GET'])
def focuser_status():
    """ Report on current status of focusing unit """
    response = {}
    delim = b' = '
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'GETSTATUS')
            data = s.recv(1024)
            lines = data.split(b'\n')
            for line in lines:
                if delim in line:
                    key, val = line.split(delim)
                    key = despace(key).strip()
                    response[key.decode()] = val.decode().strip()
    except (ConnectionRefusedError, ConnectionResetError):
        response = {}
    except Exception as e:
        response = {}
        print(f'Error: {e}')
    return jsonify(response)

if __name__ == '__main__':
    app.run()
