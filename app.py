from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bounty(base_score):
    primary_ranges = [
        (0.1, 3.9, 50, 250),
        (4, 6.9, 250, 600),
        (7, 8.9, 600, 1200),
        (9, 10, 1200, 3500)
    ]

    secondary_ranges = [
        (0.1, 3.9, 50, 125),
        (4, 6.9, 125, 300),
        (7, 8.9, 300, 600),
        (9, 10, 600, 1750)
    ]

    primary_bounty, secondary_bounty = 0, 0

    for score_range, primary_range, secondary_range in zip(primary_ranges, primary_ranges, secondary_ranges):
        if score_range[0] <= base_score <= score_range[1]:
            primary_bounty = primary_range[2] + (base_score - score_range[0]) * (primary_range[3] - primary_range[2]) / (score_range[1] - score_range[0])
            secondary_bounty = secondary_range[2] + (base_score - score_range[0]) * (secondary_range[3] - secondary_range[2]) / (score_range[1] - score_range[0])

    return primary_bounty, secondary_bounty

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    primary_result = None
    secondary_result = None

    if request.method == 'POST':
        try:
            base_score = float(request.form['base_score'])
            if 0 <= base_score <= 10:
                primary_bounty, secondary_bounty = calculate_bounty(base_score)
                primary_result = f"The calculated primary bounty amount is ${primary_bounty:.2f}"
                secondary_result = f"The calculated secondary bounty amount is ${secondary_bounty:.2f}"
            else:
                error = "Invalid CVSS score. Please enter a score between 0 and 10."
        except ValueError:
            error = "Invalid input. Please enter a valid number."

    return render_template('index.html', error=error, primary_result=primary_result, secondary_result=secondary_result)

if __name__ == '__main__':
    app.run(debug=True)
