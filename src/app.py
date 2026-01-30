from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/activities", methods=["GET"])
def get_activities():
    return jsonify(activities)

@app.route("/activities/<activity_name>/signup", methods=["POST"])
def signup(activity_name):
    email = request.args.get("email")
    if not email:
        return jsonify({"detail": "Email is required"}), 400
    activity = activities.get(activity_name)
    if not activity:
        return jsonify({"detail": "Activity not found"}), 404
    if email in activity["participants"]:
        return jsonify({"detail": "Already signed up"}), 400
    if len(activity["participants"]) >= activity["max_participants"]:
        return jsonify({"detail": "Activity is full"}), 400
    activity["participants"].append(email)
    return jsonify({"message": f"Signed up for {activity_name}"})

@app.route("/activities/<activity_name>/unregister", methods=["POST"])
def unregister(activity_name):
    email = request.args.get("email")
    if not email:
        return jsonify({"detail": "Email is required"}), 400
    activity = activities.get(activity_name)
    if not activity:
        return jsonify({"detail": "Activity not found"}), 404
    if email not in activity["participants"]:
        return jsonify({"detail": "Participant not found"}), 404
    activity["participants"].remove(email)
    return jsonify({"message": f"{email} removed from {activity_name}"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Join the basketball team and compete in local tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer Club": {
        "description": "Practice soccer skills and play matches",
        "schedule": "Mondays and Wednesdays, 3:00 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Art Club": {
        "description": "Explore various art techniques and create projects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Drama Club": {
        "description": "Participate in theater productions and improve acting skills",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Debate Team": {
        "description": "Engage in debates and improve public speaking skills",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": []
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Tuesdays, 3:00 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    }
}
