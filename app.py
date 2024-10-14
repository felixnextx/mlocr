from flask import Flask,request
from mlocr import recogniseImage
import base64

app = Flask(__name__)


@app.route('/')
def home():
    return 'mlocr v2.0'


@app.route('/base64img2mol', methods=['POST'])
def base64img2mol():
    """
Use OSRA to convert images (base64 encoded) to SDF (mol). 
    """
    ret = ""
  
    imgdata = request.json.get("img", "") 
    if imgdata != "":
        img = base64.b64decode(imgdata)
        ret = recogniseImage(img, "sdf") 

    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
