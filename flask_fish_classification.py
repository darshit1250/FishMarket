from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
pickle_in = open('fish_class.pkl','rb')
classifier = pickle.load(pickle_in)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
  int_features = [x for x in request.form.values()]
  final_features = [np.array(int_features)]
  prediction=classifier.predict(final_features)
  print(prediction)
  if (prediction[0] == 0):
      return '<h4 style="color:green">The species of this fish is <b>"Bream"</b></h4>'
  elif (prediction[0] == 1):
      return '<h4 style="color: green">The species of this fish is <b>"Parkki"</b></h4>'
  elif (prediction[0] == 2):
      return '<h4 style="color: green">The species of this fish is <b>"Perch"</b></h4>'
  elif (prediction[0] == 3):
      return '<h4 style="color: green">The species of this fish is <b>"Pike"</b></h4>'
  elif (prediction[0] == 4):
      return '<h4 style="color: green">The species of this fish is <b>"Roach"</b></h4>'
  elif (prediction[0] == 5):
      return '<h4 style="color: green">The species of this fish is <b>"Smelt"</b></h4>'
  else:
      return '<h4 style="color: green">The species of this fish is <b>"Whitefish"</b></h4>'

if __name__=='__main__':
  app.run()
