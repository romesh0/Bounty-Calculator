def calculate_bounty(score, target):
# Change the bounty range according to your company policy

    primary_ranges = {
        "Low": (0.1, 3.9, 50, 250),
        "Medium": (4, 6.9, 250, 600),
        "High": (7, 8.9, 600, 1200),
        "Critical": (9, 10, 1200, 3500)
    }

    secondary_ranges = {
        "Low": (0.1, 3.9, 50, 125),
        "Medium": (4, 6.9, 125, 300),
        "High": (7, 8.9, 300, 600),
        "Critical": (9, 10, 600, 1750)
    }

    if target == "primary":
        ranges = primary_ranges
    elif target == "secondary":
        ranges = secondary_ranges
    else:
        return None

    for level, (min_score, max_score, min_bounty, max_bounty) in ranges.items():
        if min_score <= score <= max_score:
            print(f"{level} : ${min_bounty} - ${max_bounty}")
            return round((score - min_score) / (max_score - min_score), 2) * (max_bounty - min_bounty) + min_bounty

    return None

while True:
    try:
        input_score = float(input("Enter the CVSS Score : "))
        if 0.1 <= input_score <= 10:
            break
        else:
            print("Please enter a valid score between 0.1 and 10.")
    except ValueError:
        print("Please enter a valid numerical score.")

primary_bounty = calculate_bounty(input_score, "primary")
secondary_bounty = calculate_bounty(input_score, "secondary")

if primary_bounty is not None:
    print(f"Primary Target Bounty amount for the CVSS score {input_score} is ${primary_bounty}")
    print(f"Secondary Target Bounty amount for the CVSS score {input_score} is ${secondary_bounty}")
else:
    print("Score is outside the defined ranges.")
