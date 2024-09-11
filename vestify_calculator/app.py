from flask import Flask, render_template, request

app = Flask(__name__)

# Formula -> Return on Investment (ROI)
def calculate_roi(investment, profit):
    try:
        roi = (profit - investment) / investment * 100
        return round(roi, 2)
    except ZeroDivisionError:
        return "Investment amount cannot be zero."

# Formula -> Savings Ratio
def calculate_savings_ratio(savings_total, monthly_gross_income):
    try:
       savings_ratio = (savings_total / monthly_gross_income) * 100
       return round(savings_ratio, 2)
    except ZeroDivisionError:
        return "Monthly Gross Income amount cannot be zero."

# Formula -> Debt to Income Ratio (DTI)
def calculate_dti(monthly_total_debt, monthly_gross_income):
    try:
        dti = (monthly_total_debt / monthly_gross_income) * 100
        return round(dti, 2)
    except ZeroDivisionError:
        return "Monthly Gross Income amount cannot be zero."

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

# Halaman untuk DTI
@app.route('/dti_ratio/', methods=['GET', 'POST'])
def dti_ratio():
    if request.method == 'POST':
        monthly_total_debt = float(request.form['monthly_total_debt'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        dti = calculate_dti(monthly_total_debt, monthly_gross_income)
        return render_template('dti_ratio.html', dti=dti, monthly_total_debt=monthly_total_debt, monthly_gross_income=monthly_gross_income)
    return render_template('dti_ratio.html')

if __name__ == '__main__':
    app.run(debug=True)
