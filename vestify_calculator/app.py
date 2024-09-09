from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_roi(investment, profit):
    try:
        roi = (profit - investment) / investment * 100
        return round(roi, 2)
    except ZeroDivisionError:
        return "Investment amount cannot be zero."

def calculate_savings_ratio(savings_total, monthly_gross_income):
    try:
       saving_ratio = (savings_total / monthly_gross_income) * 100
       return round(saving_ratio, 2)
    except ZeroDivisionError:
        return "Investment amount cannot be zero."

# Halaman Utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        investment = float(request.form['investment'])
        profit = float(request.form['profit'])
        roi = calculate_roi(investment, profit)
        return render_template('index.html', roi=roi, investment=investment, profit=profit)
    return render_template('index.html')

# Halaman untuk Savings Ratio
@app.route('/savings_ratio/', methods=['GET', 'POST'])
def savings_ratio():
    if request.method == 'POST':
        savings_total = float(request.form['savings_total'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        savings_ratio = calculate_savings_ratio(savings_total, monthly_gross_income)
        return render_template('savings_ratio.html', savings_ratio=savings_ratio, savings_total=savings_total, monthly_gross_income=monthly_gross_income)
    return render_template('savings_ratio.html')

if __name__ == '__main__':
    app.run(debug=True)
