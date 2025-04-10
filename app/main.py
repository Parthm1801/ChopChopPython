from fastapi import FastAPI, Request, Query
from app.schemas import GoalInput
from app.models import save_goal, get_goal, update_goal, generate_today_message

app = FastAPI()

@app.post("/goal")
def set_goal(goal: GoalInput):
    save_goal(goal)
    return {"message": "Goal saved"}

@app.put("/goal")
def update_existing_goal(goal: GoalInput):
    update_goal(goal)
    return {"message": "Goal updated"}

@app.get("/goal")
def fetch_goal(user_id: str = Query(...)):
    goal = get_goal(user_id)
    if not goal:
        return {"message": "No goal found"}
    return goal

@app.get("/motivation/today")
def get_today_message(user_id: str = Query(...)):
    message = generate_today_message(user_id)
    return {"message": message}

@app.get("/internal/refresh-daily-messages")
def refresh_daily_messages():
    from app.models import collection, generate_message

    users = collection.find({}, {"_id": 0, "user_id": 1, "goal": 1, "deadline": 1, "tone": 1})
    updated = 0

    for user in users:
        try:
            message = generate_message(user["goal"], user["deadline"], user["tone"])
            collection.update_one(
                {"user_id": user["user_id"]},
                {"$set": {"last_message": message}}
            )
            updated += 1
        except Exception as e:
            print(f"Error updating {user['user_id']}: {e}")

    return {"status": "success", "updated": updated}

@app.get("/tones")
def get_tones():
    return {
        "tones": [
            "TED talker",
            "Asian strict parent",
            "Philosopher",
            "Krishna",
            "Gym trainer",
            "Stoic master",
            "Anime Sensei"
        ]
    }