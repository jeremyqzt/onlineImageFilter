from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from ppmFliter import *


app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convertImage():
    useImg = "userImg"
    f = request.files['uploadImage']
    f.save(useImg + "/" + secure_filename(f.filename))
    test = ppmImageReader(useImg + "/" + secure_filename(f.filename)).getImage()
    print("Finished Read")
    t = ppmMeanFilter(test, 1, 1)
    print("Processing")
    t.filter()
    print("Finished Processing, writing")
    writer = ppmImageWriter(t.getFilteredImg())
    writer.writePPM(useImg + "/" + "filter_" + secure_filename(f.filename))
    print("Done")
    result = send_from_directory(useImg, "filter_" + secure_filename(f.filename), as_attachment=True)
    result.headers["x-suggested-filename"] = secure_filename(f.filename)
    return result
if __name__ == '__main__':
   app.run()