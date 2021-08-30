import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image

from flask import Flask,request,render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



# Define a flask app
app = Flask(__name__)
model=load_model('fashion.h5')

@app.route('/')
def index():
    return render_template('base.html')
@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=="POST":
        f=request.files['image']
        print('current path')
        basepath=os.path.dirname(__file__)
        print("current path",basepath)
        filename=os.path.join(basepath,'uploads',f.filename)
        print("upload folder is",filepath)
        f.save(filepath)
        
        img=image.load_img(filepath,target_size=(64,64))
        x=image.img_to_array(img)
        print(x)
        x=np.expand_dims(x,axis=0)
        print(x)
        preds=model.predict_classes(x)
        print("prediction",preds)
        index=["accessories","bags","footwear","mens wear","sunglasses","watches","womens wear"]
        res="The classified Image is: " +str(index[preds[0]])
    return res

if __name__ == "__main__":
    app.run(debug=True,threaded=False)


    
        





      