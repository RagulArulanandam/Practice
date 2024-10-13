from flask import Flask, render_template, request
import keras
from PIL import Image
import numpy as np
import json

app= Flask(__name__)

@app.route("/", methods= ["GET","POST"])
def hello():
    final_model2 = keras.models.load_model('D:/FinalYearProject/CLD Prediction WebApp/Model/Cassava_best_modelEffNetB3v3.h5')
    predictions = []
    IMG_SIZE = 380
    IMG_SIZE1 = 300
    # size = (IMG_SIZE,IMG_SIZE)
    size1= (IMG_SIZE1,IMG_SIZE1)
    #for image in test_images:
    if request.method == "POST":
        file = request.files['file']
        path = file.filename
        img1 = Image.open('C:/Users/arulk/OneDrive/Desktop/TestImages/' + path)
        img1 = img1.resize(size1)
        img1 = np.expand_dims(img1, axis=0)
        prediction2 = final_model2.predict(img1)
        predictions.extend(prediction2.argmax(axis = 1))
        f = open("D:/FinalYearProject/CassavaLeafDisase/cassava-leaf-disease-classification-source/label_num_to_disease_map.json")
        data = json.load(f)
        val = data["{}".format(predictions[0])]
        location = 'D:/FinalYearProject/CassavaLeafDisase/cassava-leaf-disease-classification-source/train_images/' + path
        return render_template("result.html", msg=val ,imgg=location)
    return render_template("home.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



if __name__ == '__main__':
    app.run(debug=True)