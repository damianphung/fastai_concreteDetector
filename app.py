import numpy as np

from typing import Optional
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
import pickle

#from resources.utils import *
from fastai.vision.widgets import *
from fastai.imports import *
from fastai.vision.all import *
import os

cwd = os.getcwd()
path = Path()
Path().ls(file_exts='.pkl')

application = FastAPI()
templates = Jinja2Templates(directory="templates")

model = load_learner(path/'model/export.pkl')

#Defining the home page for the web service
@application.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', { 'request' : request })

#Writing api for inference using the loaded model
@application.post('/predict')

#Predict method that uses the trained model to predict the kind of bear in the picture we uploaded
async def predict(request: Request, file: UploadFile = File(...)):
    
        #labels = ['grizzly','black','teddy']
        contents = await file.read()
        filename = file.filename
        with open(os.path.join("resources/tmp", filename), 'wb') as f:
            f.write(contents)

        filename = file.filename
        to_predict = "resources/tmp/"+filename

        #Getting the prediction from the model
        prediction = model.predict(to_predict)
        
        print(prediction)
        print(model.dls.vocab)

        print(sorted(zip(model.dls.vocab, map(float, prediction[2])), key=lambda p:p[1], reverse=True))

        #Render the result in the html template
        return templates.TemplateResponse('index.html', { 
            "request" : request, 
            "prediction_text" : "Your Prediction : {}".format(prediction[0]) } )

