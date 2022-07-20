from urllib.parse import urlencode

import requests as requests
from flask import Flask, json, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root_response():
    with open('static/jsonadmissiontest.json') as d:
        dictData = json.load(d)
    data = urlencode(dictData)
    print ('data', data)
    res = requests.post('https://test.cpnu-admission.edu.eg/webService/acceptStudent/', data, verify=False)
    print ('response from server:', res.text)
    dictFromServer = res.json()
    return dictFromServer


if __name__ == '__main__':
    app.debug = True
    app.run()
