import os
from pymongo import MongoClient
from dotenv import load_dotenv
from app.schemas import GoalInput
from app.openai_engine import generate_message

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)
db = client["chopchopai"]
collection = db["goals"]

def save_goal(goal: GoalInput):
    collection.update_one(
        {"user_id": goal.user_id},
        {
            "$set": {
                "goal": goal.goal,
                "deadline": goal.deadline,
                "tone": goal.tone,
                "last_message": None
            }
        },
        upsert=True
    )

def get_goal(user_id: str):
    return collection.find_one({"user_id": user_id}, {"_id": 0})

def update_goal(goal: GoalInput):
    save_goal(goal)

def generate_today_message(user_id: str):
    doc = get_goal(user_id)
    if not doc:
        return "No goal found for this app instance."

    message = generate_message(
        goal_text=doc["goal"],
        deadline=doc["deadline"],
        tone=doc["tone"]
    )

    collection.update_one(
        {"user_id": user_id},
        {"$set": {"last_message": message}}
    )

    return message
