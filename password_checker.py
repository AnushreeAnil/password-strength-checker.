import re

def evaluate_password(password: str):
    """Return (score_0_to_5, label, missing_criteria_list)."""
    criteria = {
        "length>=8": len(password) >= 8,
        "lowercase": bool(re.search(r"[a-z]", password)),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "digit":     bool(re.search(r"[0-9]", password)),
        "special":   bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    score = sum(1 for ok in criteria.values() if ok)

    if not criteria["length>=8"]:
        label = "Weak"
    elif score <= 2:
        label = "Weak"
    elif score == 3:
        label = "Moderate"
    else:
        label = "Strong"

    missing = [k for k, ok in criteria.items() if not ok]
    return score, label, missing

if __name__ == "__main__":
    pwd = input("Enter a password: ")
    score, label, missing = evaluate_password(pwd)
    print(f"\nPassword strength: {label} ({score}/5)")
    if missing:
        print("To improve, add:", ", ".join(missing))
