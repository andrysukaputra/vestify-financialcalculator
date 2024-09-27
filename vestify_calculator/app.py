# Main application file for Flask web application
# This file contains the main logic to serve the web pages, and
# call the functions to calculate the desired metrics.

from flask import Flask, render_template, request
import locale

# Create the Flask application
app = Flask(__name__)

locale.setlocale(locale.LC_ALL, "")


# 1. Home/First Page
@app.route('/')
def index():
    return render_template('index.html')


# 2. Formula dan Halaman ROI
# 2. Formula -> Return on Investment (ROI)

# Calculate Return on Investment (ROI) given final value of investment, initial value of investment, and cost of investment.
# ROI is calculated using the following formula: (final value of investment - initial value of investment) / cost of investment * 100
# If the cost of investment amount is zero, the function returns a string indicating this.
def calculate_roi(final_value_of_investment, initial_value_of_investment, cost_of_investment):
    """
    Calculate Return on Investment (ROI) given final value of investment, initial value of investment and cost of investment.

    :param float final value of investment: Total final value of investment amount
    :param float initial value of investment: Total initial value of investment amount
    :return: ROI, or string if error occurs
    """
    try:
        # calculate ROI using the formula
        roi = ((final_value_of_investment - initial_value_of_investment) / cost_of_investment) * 100
        # round the result to 2 decimal places
        return round(roi, 2)
    except ZeroDivisionError:
        # return a string if the investment amount is zero
        return "Cost of investment amount cannot be zero."

# 2. Halaman -> ROI    
@app.route('/roi/', methods=['GET', 'POST'])
def roi():
    """
    Halaman ini berisi kalkulator ROI (Return on Investment).

    :param float final value of investment: Total nilai akhir investasi
    :param float initial value of investment: Total nilai awal investasi
    :param float cost of investment: Total biaya investasi
    :return: Hasil ROI, total nilai akhir investasi, total nilai awal investasi, dan total biaya investasi
    """
    if request.method == 'POST':
        final_value_of_investment = float(request.form['final_value_of_investment'])
        initial_value_of_investment = float(request.form['initial_value_of_investment'])
        cost_of_investment = float(request.form['cost_of_investment'])
        roi = calculate_roi(final_value_of_investment, initial_value_of_investment, cost_of_investment)

        # Formated ROI to Local Currency
        formatted_formfinal = locale.currency(final_value_of_investment, grouping=True)
        formatted_forminitial = locale.currency(initial_value_of_investment, grouping=True)
        formatted_formcost = locale.currency(cost_of_investment, grouping=True)
        return render_template('roi.html', roi=roi, final_value_of_investment=formatted_formfinal, initial_value_of_investment=formatted_forminitial, cost_of_investment=formatted_formcost)
    return render_template('roi.html', roi=None)


# 3. Formula dan Halaman Savings Rate
# 3. Formula -> Savings Rate

# This function calculates the Savings Rate given total annual savings, employer match, and annual gross income
# The Savings Rate is calculated using the following formula: ((total_annual_savings + employer_match) / annual_gross_income) * 100
# If the annual gross income amount is zero, the function returns a string indicating this.
def calculate_sr(total_annual_savings, employer_match, annual_gross_income):
    """
    Calculate Savings Rate given total annual savings, employer match and annual gross income.

    :param float total_annual_savings: Total annual savings amount
    :param float employer_match: Employer match amount
    :param float annual_gross_income: Annual gross income
    :return: Savings Rate, or string if error occurs
    """
    try:
        # calculate Savings Rate using the formula
        sr = ((total_annual_savings + employer_match) / annual_gross_income) * 100
        # round the result to 2 decimal places
        return round(sr, 2)
    except ZeroDivisionError:
        # return a string if the monthly gross income amount is zero
        return "Annual Gross Income amount cannot be zero."

# 3. Halaman untuk Savings Rate
@app.route('/savings_rate/', methods=['GET', 'POST'])
def savings_rate():
    """
    Halaman untuk menghitung Savings Ratio.

    Savings Ratio dihitung dengan membagi jumlah total tabungan dengan pendapatan bulanan bruto.

    :param float savings_total: Jumlah total tabungan
    :param float monthly_gross_income: Pendapatan bulanan bruto
    :return: Hasil Savings Ratio, jumlah total tabungan, dan pendapatan bulanan bruto
    """
    if request.method == 'POST':
        total_annual_savings = float(request.form['total_annual_savings'])
        employer_match = float(request.form['employer_match'])
        annual_gross_income = float(request.form['annual_gross_income'])
        sr = calculate_sr(total_annual_savings, employer_match, annual_gross_income)
        
        # Formated Saving Rate to Local Currency
        formatted_formtas = locale.currency(total_annual_savings, grouping=True)
        formatted_formem = locale.currency(employer_match, grouping=True)
        formatted_formagi = locale.currency(annual_gross_income, grouping=True)
        return render_template('savings_rate.html', sr=sr, total_annual_savings=formatted_formtas, employer_match=formatted_formem, annual_gross_income=formatted_formagi)
    return render_template('savings_rate.html')


# 4. Formula dan Halaman Debt to Income Ratio
# 4. Formula -> Debt to Income Ratio (DTI)

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

# 4. Halaman untuk DTI
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

        # Formated DTI to Local Currency
        formatted_formmtd = locale.currency(monthly_total_debt, grouping=True)
        formatted_formmgi = locale.currency(monthly_gross_income, grouping=True)
        return render_template('dti_ratio.html', dti=dti, monthly_total_debt=formatted_formmtd, monthly_gross_income=formatted_formmgi)
    return render_template('dti_ratio.html')


# 5. Formula dan Halaman Emergency Fund Ratio
# 5. Formula -> Emergency Fund Ratio

# This function calculates the Emergency Fund Ratio (EFR) given emergency cash fund and monthly primary expenses
# The EFR is calculated using the following formula: (emergency_cash_fund / monthly_primary_expenses)
# If the monthly primary expenses amount is zero, the function returns a string indicating this.
def calculate_efr(emergency_cash_fund, monthly_primary_expenses):
    """
    Calculate Emergency Fund Ratio (EFR) given emergency fund and monthly expenses.

    :param float emergency_fund: Total emergency fund amount
    :param float monthly_expenses: Monthly expenses
    :return: EFR, or string if error occurs
    """
    try:
        # calculate EFR using the formula
        efr = (emergency_cash_fund / monthly_primary_expenses)
        # round the result to 2 decimal places
        return round(efr, 2)
    except ZeroDivisionError:
        # return a string if the monthly primary expenses is zero
        return "Monthly Primary Expenses amount cannot be zero."

# 5. Halaman untuk Emergency Fund Ratio
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
        emergency_cash_fund = float(request.form['emergency_cash_fund'])
        monthly_primary_expenses = float(request.form['monthly_primary_expenses'])
        efr = calculate_efr(emergency_cash_fund, monthly_primary_expenses)

        # Formated EFR to Local Currency
        formatted_formecf = locale.currency(emergency_cash_fund, grouping=True)
        formatted_formmpe = locale.currency(monthly_primary_expenses, grouping=True)
        return render_template('emergency_fund_ratio.html', efr=efr, emergency_cash_fund=formatted_formecf, monthly_primary_expenses=formatted_formmpe)
    return render_template('emergency_fund_ratio.html')


# 6. Formula dan Halaman Liquidity Ratio
# 6. Formula -> Liquidity Ratio

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

# 6. Halaman untuk Liquidity Ratio
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

        # Formated LR to Local Currency
        formatted_formca = locale.currency(current_assets, grouping=True)
        formatted_formme = locale.currency(monthly_expenses, grouping=True)
        return render_template('liquidity_ratio.html', lr=lr, current_assets=formatted_formca, monthly_expenses=formatted_formme)
    return render_template('liquidity_ratio.html')


# 7. Formula dan Halaman Net Worth to Assets Ratio
# 7. Formula -> Net Worth to Assets Ratio

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

# 7. Halaman untuk Net Worth to Assets Ratio
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

        # Formated NWAR to Local Currency
        formatted_formnw = locale.currency(net_worth, grouping=True)
        formatted_formta = locale.currency(total_assets, grouping=True)
        return render_template('net_worth_to_assets_ratio.html', nwar=nwar, net_worth=formatted_formnw, total_assets=formatted_formta)
    return render_template('net_worth_to_assets_ratio.html')


# 8. Formula dan Halaman Debt to Assets Ratio
# 8. Formula -> Debt to Assets Ratio

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

# 8. Halaman untuk Debt to Assets Ratio
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

        # Formated DAR to Local Currency
        formatted_formtd = locale.currency(total_debt, grouping=True)
        formatted_formta = locale.currency(total_assets, grouping=True)
        return render_template('debt_to_assets_ratio.html', dar=dar, total_debt=formatted_formtd, total_assets=formatted_formta)
    return render_template('debt_to_assets_ratio.html')


# 9. Formula dan Halaman Assets to Total Assets Ratio
# 9. Formula -> Investment Assets to Total Assets Ratio

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

# 9. Halaman untuk Investment Assets to Total Assets Ratio
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

        # Formated IATAR to Local Currency
        formatted_formia = locale.currency(investment_assets, grouping=True)
        formatted_formta = locale.currency(total_assets, grouping=True)
        return render_template('iatar.html', iatar=iatar, investment_assets=formatted_formia, total_assets=formatted_formta)
    return render_template('iatar.html')


# 10. Formula dan Halaman Basic Housing Ratio
# 10. Formula -> Basic Housing Ratio

# This function calculates the Basic Housing Ratio (BHR) given housing costs and monthly gross income
# The BHR is calculated using the following formula: (housing_costs / monthly_gross_income) * 100
# If the monthly gross income amount is zero, the function returns a string indicating this.
def calculate_bhr(housing_costs, monthly_gross_income):
    """
    Calculate Basic Housing Ratio (BHR) given housing costs and monthly gross income.

    :param float housing_costs: Total housing costs
    :param float monthly_gross_income: Monthly gross income
    :return: BHR, or string if error occurs
    """
    try:
        # calculate BHR using the formula
        bhr = (housing_costs / monthly_gross_income) * 100
        # round the result to 2 decimal places
        return round(bhr, 2)
    except ZeroDivisionError:
        # return a string if the monthly gross income amount is zero
        return "Monthly gross income amount cannot be zero."

# 10. Halaman untuk Basic Housing Ratio
@app.route('/bhr/', methods=['GET', 'POST'])
def bhr():
    """
    Halaman untuk menghitung Basic Housing Ratio (BHR).

    BHR dihitung dengan membagi total housing costs dengan monthly gross income.

    :param float housing_costs: Total housing costs
    :param float monthly_gross_income: Monthly gross income
    :return: Hasil BHR, total housing costs, dan monthly gross income
    """
    if request.method == 'POST':
        housing_costs = float(request.form['housing_costs'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        bhr = calculate_bhr(housing_costs, monthly_gross_income)

        # Formated BHR to Local Currency
        formatted_formhc = locale.currency(housing_costs, grouping=True)
        formatted_formmgi = locale.currency(monthly_gross_income, grouping=True)
        return render_template('bhr.html', bhr=bhr, housing_costs=formatted_formhc, monthly_gross_income=formatted_formmgi)
    return render_template('bhr.html')


# 11. Formula dan Halaman Broad Housing and Other Debts Ratio
# 11. Formula -> Broad Housing and Other Debts Ratio

# This function calculates the Broad Housing and Other Debts Ratio (BHODR) given broad housing and other debts
# The BHODR is calculated using the following formula: ((housing_costs + other_debt_payments) / monthly_gross_income) * 100
# If the monthly gross income amount is zero, the function returns a string indicating this.
def calculate_bhodr(housing_costs, other_debt_payments, monthly_gross_income):
    """
    Calculate Broad Housing and Other Debts Ratio (BHODR) given housing costs, other debt payments, and monthly gross income.

    :param float housing_costs: Total housing costs
    :param float other_debt_payments: Total other debt payments
    :param float monthly_gross_income: Monthly gross income
    :return: BHODR, or string if error occurs
    """
    try:
        # calculate BHODR using the formula
        bhodr = ((housing_costs + other_debt_payments) / monthly_gross_income) * 100
        # round the result to 2 decimal places
        return round(bhodr, 2)
    except ZeroDivisionError:
        # return a string if the monthly gross income amount is zero
        return "Monthly gross income amount cannot be zero."

# 11. Halaman untuk Broad Housing and Other Debts Ratio
@app.route('/bhodr/', methods=['GET', 'POST'])
def bhodr():
    """
    Halaman untuk menghitung Broad Housing and Other Debts Ratio (BHR).

    BHR dihitung dengan menjumlah total housing costs dengan other debt payments dan membaginya dengan monthly gross income.

    :param float housing_costs: Total housing costs
    :param float other_debt_payments: Other debt payments
    :param float monthly_gross_income: Monthly gross income
    :return: Hasil BHR, total housing costs, other debt payments dan monthly gross income
    """
    if request.method == 'POST':
        housing_costs = float(request.form['housing_costs'])
        other_debt_payments = float(request.form['other_debt_payments'])
        monthly_gross_income = float(request.form['monthly_gross_income'])
        bhodr = calculate_bhodr(housing_costs, other_debt_payments,monthly_gross_income)

        # Formated BHODR to Local Currency
        formatted_formhc = locale.currency(housing_costs, grouping=True)
        formatted_formodp = locale.currency(other_debt_payments, grouping=True)
        formatted_formmgi = locale.currency(monthly_gross_income, grouping=True)
        return render_template('bhodr.html', bhodr=bhodr, housing_costs=formatted_formhc, other_debt_payments=formatted_formodp, monthly_gross_income=formatted_formmgi)
    return render_template('bhodr.html')


# 12. Formula dan Halaman Investment Assets to Gross Pay Ratio
# 12. Formula -> Investment Assets to Gross Pay Ratio

# This function calculates the Investment Assets to Gross Pay Ratio (IAGPR) given investment assets, cash and annual gross pay
# The IAGPR is calculated using the following formula: ((investment_assets + cash) / annual_gross_pay) * 100
# If the annual gross pay amount is zero, the function returns a string indicating this.
def calculate_iagpr(investment_assets, cash, annual_gross_pay):
    """
    Calculate Investment Assets to Gross Pay Ratio (IAGPR) given investment assets, cash, and annual gross pay.

    :param float investment_assets: Total investment assets
    :param float cash: Total cash
    :param float annual_gross_pay: Annual gross pay
    :return: IAGPR, or string if error occurs
    """
    try:
        # calculate IAGPR using the formula
        iagpr = ((investment_assets + cash) / annual_gross_pay) * 100
        # round the result to 2 decimal places
        return round(iagpr, 2)
    except ZeroDivisionError:
        # return a string if the annual gross pay amount is zero
        return "Annual gross pay amount cannot be zero."

# 12. Halaman untuk Investment Assets to Gross Pay Ratio
@app.route('/iagpr/', methods=['GET', 'POST'])
def iagpr():
    """
    Halaman untuk menghitung Investment Assets to Gross Pay Ratio (IAGPR).

    IAGPR dihitung dengan membagi total investment assets, cash, dan membaginya dengan monthly gross income.

    :param float investment_assets: Total investment assets
    :param float cash: Total cash
    :param float annual_gross_income: Total annual gross income
    :return: Hasil IAGPR, total investment assets, cash, dan annual gross income
    """
    if request.method == 'POST':
        investment_assets = float(request.form['investment_assets'])
        cash = float(request.form['cash'])
        annual_gross_income = float(request.form['annual_gross_income'])
        iagpr = calculate_iagpr(investment_assets, cash, annual_gross_income)

        # Formated IAGPR to Local Currency
        formatted_formia = locale.currency(investment_assets, grouping=True)
        formatted_formc = locale.currency(cash, grouping=True)
        formatted_formagi = locale.currency(annual_gross_income, grouping=True)
        return render_template('iagpr.html', iagpr=iagpr, investment_assets=formatted_formia, cash=formatted_formc, annual_gross_income=formatted_formagi)
    return render_template('iagpr.html')


if __name__ == '__main__':
    app.run(debug=True)
