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
    useImg = "userImg"
    f = request.files["uploadImage"]
    width = int(request.form["filterW"])
    fp = useImg + "/" + secure_filename(f.filename)
    f.save(fp)
    filterType = request.form["filterT"]
    converterAdaptor = serverFilterAdaptor(width, filterType, useImg, secure_filename(f.filename))
    retName = converterAdaptor.process()
    result = send_from_directory(useImg, retName, as_attachment=True)
    result.headers["x-suggested-filename"] = retName
    os.remove(fp)
    return result


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)