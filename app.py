from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bounty(base_score):
    primary_bounty, secondary_bounty = 0, 0

    if 0.1 <= base_score <= 3.9:
        primary_bounty = 50 + (base_score - 0.1) * 50
        secondary_bounty = 50 + (base_score - 0.1) * 75
    elif 4 <= base_score <= 6.9:
        primary_bounty = 250 + (base_score - 4) * 75
        secondary_bounty = 125 + (base_score - 4) * 50
    elif 7 <= base_score <= 8.9:
        primary_bounty = 600 + (base_score - 7) * 150
        secondary_bounty = 300 + (base_score - 7) * 100
    elif 9 <= base_score <= 10:
        primary_bounty = 1201 + (base_score - 9) * 880
        secondary_bounty = 600 + (base_score - 9) * 1150

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
