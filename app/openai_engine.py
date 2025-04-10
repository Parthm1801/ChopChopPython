from openai import OpenAI
from app.utils import compute_days_left
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_message(goal_text, deadline, tone):
    days_left = compute_days_left(deadline)
    prompt = f"""
    You are a motivational assistant, who needs to generate a message in second person (addressing the user as 'you') in the given tone. You can take inspiration from quotes available online too, and fit that in the context.
    Goal: {goal_text}
    Deadline: {deadline} (in {days_left} days)
    Tone: {tone}

    Generate a motivational message that becomes more urgent as the deadline approaches. The message should be very short not exceeding 20 words.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )

    return response.choices[0].message.content.strip()
