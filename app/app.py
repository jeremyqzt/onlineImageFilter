#!/usr/bin/python3

from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from serverFilterAdaptor import *
import os

app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convertImage():
    userImg = "userImg"
    f = request.files["uploadImage"]
    width = int(request.form["filterW"])
    fp = "%s/%s" %(userImg, secure_filename(f.filename))
    f.save(fp)
    filterType = int(request.form["filterT"])
    converterAdaptor = serverFilterAdaptor(width, filterType, userImg, secure_filename(f.filename))
    retName = converterAdaptor.process()
    if (retName != None):
        result = send_from_directory(userImg, retName, as_attachment=True)
        result.headers["x-suggested-filename"] = retName
    else:
        result = "An Error has Occurred"
    return result


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=8000)