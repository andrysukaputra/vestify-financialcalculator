# Main application file for Flask web application
# This file contains the main logic to serve the web pages, and
# call the functions to calculate the desired metrics.

from flask import Flask, render_template, request

# Create the Flask application
app = Flask(__name__)


""" 
---Personal Finance Formulas Section---
"""

# Formula -> Return on Investment (ROI)

# Calculate Return on Investment (ROI) given investment and profit.
# ROI is calculated using the following formula: (profit - investment) / investment * 100
# If the investment amount is zero, the function returns a string indicating this.
def calculate_roi(investment, profit):
    """
    Calculate Return on Investment (ROI) given investment and profit.

    :param float investment: Total investment amount
    :param float profit: Total profit amount
    :return: ROI, or string if error occurs
    """
    try:
        # calculate ROI using the formula
        roi = (profit - investment) / investment * 100
        # round the result to 2 decimal places
        return round(roi, 2)
    except ZeroDivisionError:
        # return a string if the investment amount is zero
        return "Investment amount cannot be zero."


# Formula -> Savings Ratio

# This function calculates the Savings Ratio given total savings and monthly gross income
# The Savings Ratio is calculated using the following formula: (savings_total / monthly_gross_income) * 100
# If the monthly gross income amount is zero, the function returns a string indicating this.
def calculate_savings_ratio(savings_total, monthly_gross_income):
    """
    Calculate Savings Ratio given total savings and monthly gross income.

    :param float savings_total: Total savings amount
    :param float monthly_gross_income: Monthly gross income
    :return: Savings Ratio, or string if error occurs
    """
    try:
        # calculate Savings Ratio using the formula
        savings_ratio = (savings_total / monthly_gross_income) * 100
        # round the result to 2 decimal places
        return round(savings_ratio, 2)
    except ZeroDivisionError:
        # return a string if the monthly gross income amount is zero
        return "Monthly Gross Income amount cannot be zero."


# Formula -> Debt to Income Ratio (DTI)

# This function calculates the Debt to Income Ratio (DTI) given total debt and monthly gross income
# The DTI is calculated using the following formula: (monthly_total_debt / monthly_gross_income) * 100
# If the monthly gross income amount is zero, the function returns a string indicating this.
def calculate_dti(monthly_total_debt, monthly_gross_income):
    """
    Calculate Debt to Income Ratio (DTI) given total debt and monthly gross income.

    :param float monthly_total_debt: Total debt amount
    :param float monthly_gross_income: Monthly gross income
    :return: DTI, or string if error occurs
    """
    try:
        # calculate DTI using the formula
        dti = (monthly_total_debt / monthly_gross_income) * 100
        # round the result to 2 decimal places
        return round(dti, 2)
    except ZeroDivisionError:
        # return a string if the monthly gross income amount is zero
        return "Monthly Gross Income amount cannot be zero."


# Formula -> Emergency Fund Ratio

# This function calculates the Emergency Fund Ratio (EFR) given emergency fund and monthly expenses
# The EFR is calculated using the following formula: (emergency_fund / monthly_expenses)
# If the monthly expenses amount is zero, the function returns a string indicating this.
def calculate_efr(emergency_fund, monthly_expenses):
    """
    Calculate Emergency Fund Ratio (EFR) given emergency fund and monthly expenses.

    :param float emergency_fund: Total emergency fund amount
    :param float monthly_expenses: Monthly expenses
    :return: EFR, or string if error occurs
    """
    try:
        # calculate EFR using the formula
        efr = (emergency_fund / monthly_expenses)
        # round the result to 2 decimal places
        return round(efr, 2)
    except ZeroDivisionError:
        # return a string if the monthly expenses is zero
        return "Monthly Expenses amount cannot be zero."


# Formula -> Liquidity Ratio

# This function calculates the Liquidity Ratio (LR) given current assets and monthly expenses
# The LR is calculated using the following formula: (current_assets / monthly_expenses)
# If the monthly expenses amount is zero, the function returns a string indicating this.
def calculate_lr(current_assets, monthly_expenses):
    """
    Calculate Liquidity Ratio (LR) given current assets and monthly expenses.

    :param float current_assets: Total current assets
    :param float monthly_expenses: Monthly expenses
    :return: LR, or string if error occurs
    """
    try:
        # calculate LR using the formula
        lr = (current_assets / monthly_expenses)
        # round the result to 2 decimal places
        return round(lr, 2)
    except ZeroDivisionError:
        # return a string if the monthly expenses is zero
        return "Monthly expenses amount cannot be zero."


# Formula -> Net Worth to Assets Ratio

# This function calculates the Net Worth to Assets Ratio (NWAR) given net worth and total assets
# The NWAR is calculated using the following formula: (net_worth / total_assets) * 100
# If the total assets amount is zero, the function returns a string indicating this.
def calculate_nwar(net_worth, total_assets):
    """
    Calculate Net Worth to Assets Ratio (NWAR) given net worth and total assets.

    :param float net_worth: Total net worth
    :param float total_assets: Total assets
    :return: NWAR, or string if error occurs
    """
    try:
        # calculate NWAR using the formula
        nwar = (net_worth / total_assets) * 100
        # round the result to 2 decimal places
        return round(nwar, 2)
    except ZeroDivisionError:
        # return a string if the total assets amount is zero
        return "Total assets amount cannot be zero."


# Formula -> Debt to Assets Ratio

# This function calculates the Debt to Assets Ratio (DAR) given total debt and total assets
# The DAR is calculated using the following formula: (total_debt / total_assets) * 100
# If the total assets amount is zero, the function returns a string indicating this.
def calculate_dar(total_debt, total_assets):
    """
    Calculate Debt to Assets Ratio (DAR) given total debt and total assets.

    :param float total_debt: Total debt
    :param float total_assets: Total assets
    :return: DAR, or string if error occurs
    """
    try:
        # calculate DAR using the formula
        dar = (total_debt / total_assets) * 100
        # round the result to 2 decimal places
        return round(dar, 2)
    except ZeroDivisionError:
        # return a string if the total assets amount is zero
        return "Total assets amount cannot be zero."


# Formula -> Investment Assets to Total Assets Ratio

# This function calculates the Investment Assets to Total Assets Ratio (IATAR) given investment assets and total assets
# The IATAR is calculated using the following formula: (investment_assets / total_assets) * 100
# If the total assets amount is zero, the function returns a string indicating this.
def calculate_iatar(investment_assets, total_assets):
    """
    Calculate Investment Assets to Total Assets Ratio (IATAR) given investment assets and total assets.

    :param float investment_assets: Total investment assets
    :param float total_assets: Total assets
    :return: IATAR, or string if error occurs
    """
    try:
        # calculate IATAR using the formula
        iatar = (investment_assets / total_assets) * 100
        # round the result to 2 decimal places
        return round(iatar, 2)
    except ZeroDivisionError:
        # return a string if the total assets amount is zero
        return "Total assets amount cannot be zero."


# Formula -> 


""" 
---Flask App Pages to HTML Section---
"""

# 1. Halaman Utama
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Halaman Utama.

    Halaman ini berisi kalkulator investasi, yaitu ROI (Return on Investment).

    :param float investment: Jumlah investasi
    :param float profit: Jumlah keuntungan
    :return: Hasil ROI, jumlah investasi, dan jumlah keuntungan
    """
    if request.method == 'POST':
        investment = float(request.form['investment'])
        profit = float(request.form['profit'])
        roi = calculate_roi(investment, profit)
        return render_template('index.html', roi=roi, investment=investment, profit=profit)
    return render_template('index.html')

# 2. Halaman untuk Savings Ratio
@app.route('/savings_ratio/', methods=['GET', 'POST'])
def savings_ratio():
    """
    Halaman untuk menghitung Savings Ratio.

    Savings Ratio dihitung dengan membagi jumlah total tabungan dengan pendapatan bulanan bruto.

    :param float savings_total: Jumlah total tabungan
    :param float monthly_gross_income: Pendapatan bulanan bruto
    :return: Hasil Savings Ratio, jumlah total tabungan, dan pendapatan bulanan bruto
    """
    if request.method == 'POST':
        savings_total = float(request.form['savings_total'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        savings_ratio = calculate_savings_ratio(savings_total, monthly_gross_income)
        return render_template('savings_ratio.html', savings_ratio=savings_ratio, savings_total=savings_total, monthly_gross_income=monthly_gross_income)
    return render_template('savings_ratio.html')

# 3. Halaman untuk DTI
@app.route('/dti_ratio/', methods=['GET', 'POST'])
def dti_ratio():
    """
    Halaman untuk menghitung Debt to Income Ratio (DTI).

    DTI dihitung dengan membagi jumlah total utang bulanan dengan pendapatan bulanan bruto.

    :param float monthly_total_debt: Jumlah total utang bulanan
    :param float monthly_gross_income: Pendapatan bulanan bruto
    :return: Hasil DTI, jumlah total utang bulanan, dan pendapatan bulanan bruto
    """
    if request.method == 'POST':
        monthly_total_debt = float(request.form['monthly_total_debt'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        dti = calculate_dti(monthly_total_debt, monthly_gross_income)
        return render_template('dti_ratio.html', dti=dti, monthly_total_debt=monthly_total_debt, monthly_gross_income=monthly_gross_income)
    return render_template('dti_ratio.html')

# 4. Halaman untuk Emergency Fund Ratio
@app.route('/emergency_fund_ratio/', methods=['GET', 'POST'])
def emergency_fund_ratio():
    """
    Halaman untuk menghitung Emergency Fund Ratio (EFR).

    EFR dihitung dengan membagi jumlah dana darurat dengan pengeluaran bulanan.

    :param float emergency_fund: Jumlah dana darurat
    :param float monthly_expenses: Pengeluaran bulanan
    :return: Hasil EFR, dana darurat, dan pengeluaran bulanan
    """
    if request.method == 'POST':
        emergency_fund = float(request.form['emergency_fund'])
        monthly_expenses = float(request.form['monthly_expenses'])
        efr = calculate_efr(emergency_fund, monthly_expenses)
        return render_template('emergency_fund_ratio.html', efr=efr, emergency_fund=emergency_fund, monthly_expenses=monthly_expenses)
    return render_template('emergency_fund_ratio.html')

# 5. Halaman untuk Liquidity Ratio
@app.route('/liquidity_ratio/', methods=['GET', 'POST'])
def liquidity_ratio():
    """
    Halaman untuk menghitung Liquidity Ratio (LR).

    LR dihitung dengan membagi current assets dengan monthly expenses.

    :param float current_assets: Jumlah current assets
    :param float monthly_expenses: Pengeluaran bulanan
    :return: Hasil LR, current assets, dan monthly expenses
    """
    if request.method == 'POST':
        current_assets = float(request.form['current_assets'])
        monthly_expenses = float(request.form['monthly_expenses'])
        lr = calculate_lr(current_assets, monthly_expenses)
        return render_template('liquidity_ratio.html', lr=lr, current_assets=current_assets, monthly_expenses=monthly_expenses)
    return render_template('liquidity_ratio.html')

# 6. Halaman untuk Net Worth to Assets Ratio
@app.route('/net_worth_to_assets_ratio/', methods=['GET', 'POST'])
def net_worth_to_assets_ratio():
    """
    Halaman untuk menghitung Net Worth to Assets Ratio (NWAR).

    NWAR dihitung dengan membagi total net worth dengan total assets.

    :param float net_worth: Total net worth
    :param float total_assets: Total assets
    :return: Hasil NWAR, total net worth, dan total assets
    """
    if request.method == 'POST':
        net_worth = float(request.form['net_worth'])
        total_assets = float(request.form['total_assets'])
        nwar = calculate_nwar(net_worth, total_assets)
        return render_template('net_worth_to_assets_ratio.html', nwar=nwar, net_worth=net_worth, total_assets=total_assets)
    return render_template('net_worth_to_assets_ratio.html')

# 7. Halaman untuk Debt to Assets Ratio
@app.route('/debt_to_assets_ratio/', methods=['GET', 'POST'])
def debt_to_assets_ratio():
    """
    Halaman untuk menghitung Debt to Assets Ratio (DAR).

    DAR dihitung dengan membagi total utang dengan total assets.

    :param float total_debt: Total utang
    :param float total_assets: Total assets
    :return: Hasil DAR, total utang, dan total assets
    """
    if request.method == 'POST':
        total_debt = float(request.form['total_debt'])
        total_assets = float(request.form['total_assets'])
        dar = calculate_dar(total_debt, total_assets)
        return render_template('debt_to_assets_ratio.html', dar=dar, total_debt=total_debt, total_assets=total_assets)
    return render_template('debt_to_assets_ratio.html')

# 8. Halaman untuk Investment Assets to Total Assets Ratio
@app.route('/iatar/', methods=['GET', 'POST'])
def iatar():
    """
    Halaman untuk menghitung Investment Assets to Total Assets Ratio (IATAR).

    IATAR dihitung dengan membagi total investment assets dengan total assets.

    :param float investment_assets: Total investment assets
    :param float total_assets: Total assets
    :return: Hasil IATAR, total investment assets, dan total assets
    """
    if request.method == 'POST':
        investment_assets = float(request.form['investment_assets'])
        total_assets = float(request.form['total_assets'])
        iatar = calculate_iatar(investment_assets, total_assets)
        return render_template('iatar.html', iatar=iatar, investment_assets=investment_assets, total_assets=total_assets)
    return render_template('iatar.html')


if __name__ == '__main__':
    app.run(debug=True)
