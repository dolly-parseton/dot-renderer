from flask import Flask, request, send_file
import logging
from graphviz import Source
import requests
import tempfile

app = Flask(__name__)

@app.route("/")
def index():
    return "Use /render/<dot_url> to provide an encoded url"

@app.route("/render", methods=['GET'])
def render():
    args = request.args
    url = args.get('url')
    # logging.info('Request to base page, /')
    dot_data = requests.get(url)
    print(dot_data)
    temp = tempfile.mktemp('')
    s = Source(dot_data.text, filename=temp, format="png")
    s.render(temp, format='png')
    return send_file(temp+'.png', mimetype='image/png')
    # if dot_data.status_code == 200:
    #     return dot_data.text
    # else:
    #     return "Nothing"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
