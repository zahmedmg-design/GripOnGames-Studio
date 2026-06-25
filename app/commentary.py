import random

GOAL_LINES = [
    "GOAL! A brilliant finish and the crowd goes wild!",
    "GOAL! The keeper had no chance from that strike!",
    "GOAL! What a moment in this simulation match!",
]


def goal_commentary(team: str, minute: str) -> str:
    return f"{random.choice(GOAL_LINES)}\n{team} score at {minute}."
