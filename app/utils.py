from datetime import datetime

def compute_days_left(deadline_str: str) -> int:
    try:
        if len(deadline_str) == 4:
            target = datetime.strptime(deadline_str, "%Y")
        elif len(deadline_str) == 7:
            target = datetime.strptime(deadline_str, "%Y-%m")
        else:
            target = datetime.strptime(deadline_str, "%Y-%m-%d")
        today = datetime.today()
        return max((target - today).days, 0)
    except:
        return 9999
