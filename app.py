from flask import Flask, render_template, request, jsonify
from GarbageTruck_Routing.GarbageTruck_Routing import generate_truck_activity
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(
    __name__,
    template_folder="myhackathon",
    static_folder="myhackathon/static"
)

uri = "mongodb+srv://wasteMgmt_admin:gxh6JRtpDJmNcS2o@cluster0.sdjio.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Connect to the MongoDB database and collection
db = client["waste_management"]
images_collection = db["truck_images"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

@app.route('/')
def home():
    return render_template('superadmin.html')

@app.route('/truckList')
def dashboard():
    activities = [{"id": 1, "name": "T001"}, {"id": 2, "name": "T002"}, {"id": 3, "name": "T003"}]
    return render_template('truckList.html', activities=activities)

@app.route('/truckActivity/<int:activity_id>')
def truck_activity(activity_id):
    # Run GarbageTruck_Routing program for each truckID independently
    log, map_image = generate_truck_activity()

    return render_template(
        'truckActivity.html',
        activity_id=activity_id,
        log=log,
        map_image=map_image
    )

@app.route('/saveImage', methods=['POST'])
def save_image():
    data = request.json
    image_data = data.get("image")
    truck_id = data.get("truck_id")

    if not image_data or not truck_id:
        return jsonify({"error": "Invalid data"}), 400

    # Save image data to MongoDB
    images_collection.insert_one({
        "truck_id": truck_id,
        "image": image_data
    })

    return jsonify({"message": "Image saved successfully!"}), 201

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')


if __name__ == '__main__':
    app.run(debug=True)
