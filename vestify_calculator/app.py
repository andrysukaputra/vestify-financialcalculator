# Import resources from Flask = web app, Locale = for local currency
from flask import Flask, render_template, request
import locale

# Create the Flask application
app = Flask(__name__)

# Set locale to local currency
locale.setlocale(locale.LC_ALL, "")

# Page Contents
"""
Vestify App - Personal Finance Calculator
Content:
1. Index -> Home
2. Features -> SR, EFR, BHR, BHODR, DAR, NWAR, ROI, IAGPR
3. Savings Rate (SR)
---> SR = ((annual savings + employer match) / annual gross income) * 100
4. Emergency Fund Ratio (EFR)
---> EFR = (emergency cash fund / monthly primary expenses) * 100
5. Basic Housing Ratio (BHR)
---> BHR = (housing costs / gross income) * 100
6. Broad Housing and Other Debts Ratio (BHODR)
---> BHODR = (housing costs + other debt payments) / gross income) * 100
7. Debt to Assets Ratio (DAR)
---> DAR = (total debt / total assets) * 100
8. Net Worth to Assets Ratio (NWAR)
---> NWAR = ((total assets - liabilities) / total assets) * 100
9. Return on Investments Ratio (ROI)
---> ROI = ((ending investments - beginning investments) / beginning investments) * 100
10. Investment Assets to Gross Pay Ratio (IAGPR)
---> IAGPR = ((investment assets + cash) / annual gross income) * 100
"""

#------------------------Beginning Index Page------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
#-------------------------End Index Page--------------------------

#------------------------Beginning Features Page------------------------
@app.route("/features/", methods=["GET", "POST"])
def features():
    return render_template("features.html")
#-------------------------End Features Page--------------------------

#------------------------Beginning Savings Rate Page------------------------
# Savings Rate Formula
"""
SR = ((annual savings + employer match) / annual gross income) * 100
"""
def calculate_sr(annual_savings, employer_match, annual_gross_income):
    try:
        sr = ((annual_savings + employer_match) / annual_gross_income) * 100
        return round(sr, 2)
    except ZeroDivisionError:
        return "Annual Gross Income amount cannot be zero."

# Savings Rate %Distribution
# Annual Savings Distribution
def calculate_annual_savings_dist(annual_savings, employer_match, annual_gross_income):
    try:
        annual_savings_dist = (annual_savings / (annual_savings + employer_match + annual_gross_income)) * 100
        return round(annual_savings_dist, 2)
    except ZeroDivisionError:
        return "Annual Savings amount cannot be zero."

# Employer Match Distribution
def calculate_employer_match_dist(annual_savings, employer_match, annual_gross_income):
    try:
        employer_match_dist = (employer_match / (annual_savings + employer_match + annual_gross_income)) * 100
        return round(employer_match_dist, 2)
    except ZeroDivisionError:
        return "Employer Match amount cannot be zero."

# Annual Gross Income Distribution
def calculate_annual_gross_income_dist(annual_savings, employer_match, annual_gross_income):
    try:
        annual_gross_income_dist = (annual_gross_income / (annual_savings + employer_match + annual_gross_income)) * 100
        return round(annual_gross_income_dist, 2)
    except ZeroDivisionError:
        return "Annual Gross Income amount cannot be zero."

# Savings Rate Route HTML
@app.route("/sr/", methods = ["GET", "POST"])
def sr():
    if request.method == "POST":
        annual_savings = float(request.form["annual_savings"])
        employer_match = float(request.form["employer_match"])
        annual_gross_income = float(request.form["annual_gross_income"])
        sr = calculate_sr(annual_savings, employer_match, annual_gross_income)

        # Savings Rate %Distribution
        annual_savings_dist = calculate_annual_savings_dist(annual_savings, employer_match, annual_gross_income)
        employer_match_dist = calculate_employer_match_dist(annual_savings, employer_match, annual_gross_income)
        annual_gross_income_dist = calculate_annual_gross_income_dist(annual_savings, employer_match, annual_gross_income)

        # Format Savings Rate to Local Currency
        formatted_formtas = locale.currency(annual_savings, grouping=True)
        formatted_formem = locale.currency(employer_match, grouping=True)
        formatted_formagi = locale.currency(annual_gross_income, grouping=True)
        return render_template("sr.html", sr = sr, 
                               annual_savings = formatted_formtas, 
                               employer_match = formatted_formem, 
                               annual_gross_income = formatted_formagi,
                               annual_savings_dist = annual_savings_dist,
                               employer_match_dist = employer_match_dist,
                               annual_gross_income_dist = annual_gross_income_dist
                               )
    return render_template("sr.html", sr = None)
#--------------------------End Savings Rate Page--------------------------

#------------------------Beginning Emergency Fund Ratio Page------------------------
# Emergency Fund Ratio Formula
"""
EFR = (emergency cash fund / monthly primary expenses) * 100
"""
def calculate_efr(emergency_cash_fund, monthly_primary_expenses):
    try:
        efr = (emergency_cash_fund / monthly_primary_expenses) * 100
        return round(efr, 2)
    except ZeroDivisionError:
        return "Monthly Primary Expenses amount cannot be zero."

# Emergency Fund Ratio %Distribution
# Emergency Cash Fund Distribution
def calculate_emergency_cash_fund_dist(emergency_cash_fund, monthly_primary_expenses):
    try:
        emergency_cash_fund_dist = (emergency_cash_fund / (emergency_cash_fund + monthly_primary_expenses)) * 100
        return round(emergency_cash_fund_dist, 2)
    except ZeroDivisionError:
        return "Emergency Cash Fund amount cannot be zero."

# Monthly Primary Expenses Distribution
def calculate_monthly_primary_expenses_dist(emergency_cash_fund, monthly_primary_expenses):
    try:
        monthly_primary_expenses_dist = (monthly_primary_expenses / (emergency_cash_fund + monthly_primary_expenses)) * 100
        return round(monthly_primary_expenses_dist, 2)
    except ZeroDivisionError:
        return "Monthly Primary Expenses amount cannot be zero."

# Emergency Fund Ratio Route HTML
@app.route("/efr/", methods = ["GET", "POST"])
def efr():
    if request.method == "POST":
        emergency_cash_fund = float(request.form["emergency_cash_fund"])
        monthly_primary_expenses = float(request.form["monthly_primary_expenses"])
        efr = calculate_efr(emergency_cash_fund, monthly_primary_expenses)

        # Emergency Fund Ratio %Distribution
        emergency_cash_fund_dist = calculate_emergency_cash_fund_dist(emergency_cash_fund, monthly_primary_expenses)
        monthly_primary_expenses_dist = calculate_monthly_primary_expenses_dist(emergency_cash_fund, monthly_primary_expenses)

        # Format Emergency Fund Ratio to Local Currency
        formatted_formecf = locale.currency(emergency_cash_fund, grouping=True)
        formatted_formmpe = locale.currency(monthly_primary_expenses, grouping=True)
        return render_template("efr.html", efr = efr, 
                               emergency_cash_fund = formatted_formecf, 
                               monthly_primary_expenses = formatted_formmpe,
                               emergency_cash_fund_dist = emergency_cash_fund_dist,
                               monthly_primary_expenses_dist = monthly_primary_expenses_dist
                               )
    return render_template("efr.html", efr = None)
#--------------------------End Emergency Fund Ratio Page--------------------------

#------------------------Beginning Basic Housing Ratio Page------------------------
# Basic Housing Ratio Formula
"""
BHR = (housing costs / gross income) * 100
"""
def calculate_bhr(housing_costs, gross_income):
    try:
        bhr = (housing_costs / gross_income) * 100
        return round(bhr, 2)
    except ZeroDivisionError:
        return "Gross Income amount cannot be zero."
    
# Basic Housing Ratio %Distribution
# Housing Costs Distribution
def calculate_housing_costs_dist(housing_costs, gross_income):
    try:
        housing_costs_dist = (housing_costs / (housing_costs + gross_income)) * 100
        return round(housing_costs_dist, 2)
    except ZeroDivisionError:
        return "Housing Costs amount cannot be zero."

# Gross Income Distribution
def calculate_gross_income_dist(housing_costs, gross_income):
    try:
        gross_income_dist = (gross_income / (housing_costs + gross_income)) * 100
        return round(gross_income_dist, 2)
    except ZeroDivisionError:
        return "Gross Income amount cannot be zero."

# Basic Housing Ratio Route HTML
@app.route("/bhr/", methods = ["GET", "POST"])
def bhr():
    if request.method == "POST":
        housing_costs = float(request.form["housing_costs"])
        gross_income = float(request.form["gross_income"])
        bhr = calculate_bhr(housing_costs, gross_income)

        # Basic Housing Ratio %Distribution
        housing_costs_dist = calculate_housing_costs_dist(housing_costs, gross_income)
        gross_income_dist = calculate_gross_income_dist(housing_costs, gross_income)

        # Format Basic Housing Ratio to Local Currency
        formatted_formhc = locale.currency(housing_costs, grouping=True)
        formatted_formgi = locale.currency(gross_income, grouping=True)
        return render_template("bhr.html", bhr = bhr, 
                               housing_costs = formatted_formhc, 
                               gross_income = formatted_formgi,
                               housing_costs_dist = housing_costs_dist,
                               gross_income_dist = gross_income_dist
                               )
    return render_template("bhr.html", bhr = None)
#--------------------------End Basic Housing Ratio Page--------------------------

#------------------------Beginning Broad Housing and Other Debts Ratio Page------------------------
# Broad Housing and Other Debts Ratio Formula
"""
BHODR = (housing costs + other debt payments) / gross income) * 100
"""
def calculate_bhodr(housing_costs, other_debt_payments, gross_income):
    try:
        bhodr = (housing_costs + other_debt_payments) / gross_income) * 100
        return round(bhodr, 2)
    except ZeroDivisionError:
        return "Gross Income amount cannot be zero."

# Broad Housing and Other Debts Ratio %Distribution
# Housing Costs Distribution
def calculate_housing_costs_dist(housing_costs, other_debt_payments, gross_income):
    try:
        housing_costs_dist = (housing_costs / (housing_costs + other_debt_payments + gross_income)) * 100
        return round(housing_costs_dist, 2)
    except ZeroDivisionError:
        return "Housing Costs amount cannot be zero."

# Other Debt Payments Distribution
def calculate_other_debt_payments_dist(housing_costs, other_debt_payments, gross_income):
    try:
        other_debt_payments_dist = (other_debt_payments / (housing_costs + other_debt_payments + gross_income)) * 100
        return round(other_debt_payments_dist, 2)
    except ZeroDivisionError:
        return "Other Debt Payments amount cannot be zero."

# Gross Income Distribution
def calculate_gross_income_dist(housing_costs, other_debt_payments, gross_income):
    try:
        gross_income_dist = (gross_income / (housing_costs + other_debt_payments + gross_income)) * 100
        return round(gross_income_dist, 2)
    except ZeroDivisionError:
        return "Gross Income amount cannot be zero."

# Broad Housing and Other Debts Ratio Route HTML
@app.route("/bhodr/", methods = ["GET", "POST"])
def bhodr():
    if request.method == "POST":
        housing_costs = float(request.form["housing_costs"])
        other_debt_payments = float(request.form["other_debt_payments"])
        gross_income = float(request.form["gross_income"])
        bhodr = calculate_bhodr(housing_costs, other_debt_payments, gross_income)

        # Broad Housing and Other Debts Ratio %Distribution
        housing_costs_dist = calculate_housing_costs_dist(housing_costs, other_debt_payments, gross_income)
        other_debt_payments_dist = calculate_other_debt_payments_dist(housing_costs, other_debt_payments, gross_income)
        gross_income_dist = calculate_gross_income_dist(housing_costs, other_debt_payments, gross_income)

        # Format Broad Housing and Other Debts Ratio to Local Currency
        formatted_formhc = locale.currency(housing_costs, grouping=True)
        formatted_formodp = locale.currency(other_debt_payments, grouping=True)
        formatted_formgi = locale.currency(gross_income, grouping=True)
        return render_template("bhodr.html", bhodr = bhodr, 
                               housing_costs = formatted_formhc, 
                               other_debt_payments = formatted_formodp,
                               gross_income = formatted_formgi,
                               housing_costs_dist = housing_costs_dist,
                               other_debt_payments_dist = other_debt_payments_dist,
                               gross_income_dist = gross_income_dist
                               )
    return render_template("bhodr.html", bhodr = None)
#--------------------------End Broad Housing and Other Debts Ratio Page------------------------

#------------------------Beginning Debt to Assets Ratio Page------------------------
# Debt to Assets Ratio Formula
"""
DAR = (total debt / total assets) * 100
"""
def calculate_dar(total_debt, total_assets):
    try:
        dar = (total_debt / total_assets) * 100
        return round(dar, 2)
    except ZeroDivisionError:
        return "Total Assets amount cannot be zero."

# Debt to Assets Ratio %Distribution
# Total Debt Distribution
def calculate_total_debt_dist(total_debt, total_assets):
    try:
        total_debt_dist = (total_debt / (total_debt + total_assets)) * 100
        return round(total_debt_dist, 2)
    except ZeroDivisionError:
        return "Total Debt amount cannot be zero."

# Total Assets Distribution
def calculate_total_assets_dist(total_debt, total_assets):
    try:
        total_assets_dist = (total_assets / (total_debt + total_assets)) * 100
        return round(total_assets_dist, 2)
    except ZeroDivisionError:
        return "Total Assets amount cannot be zero."

# Debt to Assets Ratio Route HTML
@app.route("/dar/", methods = ["GET", "POST"])
def dar():
    if request.method == "POST":
        total_debt = float(request.form["total_debt"])
        total_assets = float(request.form["total_assets"])
        dar = calculate_dar(total_debt, total_assets)

        # Debt to Assets Ratio %Distribution
        total_debt_dist = calculate_total_debt_dist(total_debt, total_assets)
        total_assets_dist = calculate_total_assets_dist(total_debt, total_assets)

        # Format Debt to Assets Ratio to Local Currency
        formatted_formtd = locale.currency(total_debt, grouping=True)
        formatted_formta = locale.currency(total_assets, grouping=True)
        return render_template("dar.html", dar = dar, 
                               total_debt = formatted_formtd, 
                               total_assets = formatted_formta,
                               total_debt_dist = total_debt_dist,
                               total_assets_dist = total_assets_dist
                               )
    return render_template("dar.html", dar = None)
#--------------------------End Debt to Assets Ratio Page------------------------

#------------------------Beginning Net Worth to Assets Ratio Page------------------------
# Net Worth to Assets Ratio Formula
"""
NWAR = ((total assets - liabilities) / total assets) * 100
"""
def calculate_nwar(total_assets, liabilities):
    try:
        nwar = ((total_assets - liabilities) / total_assets) * 100
        return round(nwar, 2)
    except ZeroDivisionError:
        return "Total Assets amount cannot be zero."

# Net Worth to Assets Ratio %Distribution
# Total Assets Distribution
def calculate_total_assets_dist(total_assets, liabilities):
    try:
        total_assets_dist = (total_assets / (total_assets + liabilities)) * 100
        return round(total_assets_dist, 2)
    except ZeroDivisionError:
        return "Total Assets amount cannot be zero."

# Liabilities Distribution
def calculate_liabilities_dist(total_assets, liabilities):
    try:
        liabilities_dist = (liabilities / (total_assets + liabilities)) * 100
        return round(liabilities_dist, 2)
    except ZeroDivisionError:
        return "Liabilities amount cannot be zero."
    
# Net Worth to Assets Ratio Route HTML
@app.route("/nwar/", methods = ["GET", "POST"])
def nwar():
    if request.method == "POST":
        total_assets = float(request.form["total_assets"])
        liabilities = float(request.form["liabilities"])
        nwar = calculate_nwar(total_assets, liabilities)

        # Net Worth to Assets Ratio %Distribution
        total_assets_dist = calculate_total_assets_dist(total_assets, liabilities)
        liabilities_dist = calculate_liabilities_dist(total_assets, liabilities)

        # Format Net Worth to Assets Ratio to Local Currency
        formatted_formta = locale.currency(total_assets, grouping=True)
        formatted_formli = locale.currency(liabilities, grouping=True)
        return render_template("nwar.html", nwar = nwar, 
                               total_assets = formatted_formta, 
                               liabilities = formatted_formli,
                               total_assets_dist = total_assets_dist,
                               liabilities_dist = liabilities_dist
                               )
    return render_template("nwar.html", nwar = None)
#--------------------------End Net Worth to Assets Ratio Page------------------------

#------------------------Beginning Return on Investments Ratio Page------------------------
# Return on Investments Ratio Formula
"""
ROI = ((ending investments - beginning investments) / beginning investments) * 100
"""
def calculate_roi(ending_investments, beginning_investments):
    try:
        roi = ((ending_investments - beginning_investments) / beginning_investments) * 100
        return round(roi, 2)
    except ZeroDivisionError:
        return "Beginning Investments amount cannot be zero."

# Return on Investments Ratio %Distribution
# Ending Investments Distribution
def calculate_ending_investments_dist(ending_investments, beginning_investments):
    try:
        ending_investments_dist = (ending_investments / (ending_investments + beginning_investments)) * 100
        return round(ending_investments_dist, 2)
    except ZeroDivisionError:
        return "Ending Investments amount cannot be zero."
    
# Beginning Investments Distribution
def calculate_beginning_investments_dist(ending_investments, beginning_investments):
    try:
        beginning_investments_dist = (beginning_investments / (ending_investments + beginning_investments)) * 100
        return round(beginning_investments_dist, 2)
    except ZeroDivisionError:
        return "Beginning Investments amount cannot be zero."
    
# Return on Investments Ratio Route HTML
@app.route("/roi/", methods = ["GET", "POST"])
def roi():
    if request.method == "POST":
        ending_investments = float(request.form["ending_investments"])
        beginning_investments = float(request.form["beginning_investments"])
        roi = calculate_roi(ending_investments, beginning_investments)

        # Return on Investments Ratio %Distribution
        ending_investments_dist = calculate_ending_investments_dist(ending_investments, beginning_investments)
        beginning_investments_dist = calculate_beginning_investments_dist(ending_investments, beginning_investments)

        # Format Return on Investments Ratio to Local Currency
        formatted_formei = locale.currency(ending_investments, grouping=True)
        formatted_formbi = locale.currency(beginning_investments, grouping=True)
        return render_template("roi.html", roi = roi, 
                               ending_investments = formatted_formei, 
                               beginning_investments = formatted_formbi,
                               ending_investments_dist = ending_investments_dist,
                               beginning_investments_dist = beginning_investments_dist
                               )
    return render_template("roi.html", roi = None)
#--------------------------End Return on Investments Ratio Page------------------------

#------------------------Beginning Investment Assets to Gross Pay Ratio Page------------------------
# Investment Assets to Gross Pay Ratio Formula
"""
IAGPR = ((investment assets + cash) / annual gross income) * 100
"""
def calculate_iagpr(investment_assets, cash, annual_gross_income):
    try:
        iagpr = ((investment_assets + cash) / annual_gross_income) * 100
        return round(iagpr, 2)
    except ZeroDivisionError:
        return "Annual Gross Income amount cannot be zero."
    
# Investment Assets to Gross Pay Ratio %Distribution
# Investment Assets Distribution
def calculate_investment_assets_dist(investment_assets, cash, annual_gross_income):
    try:
        investment_assets_dist = (investment_assets / (investment_assets + cash + annual_gross_income)) * 100
        return round(investment_assets_dist, 2)
    except ZeroDivisionError:
        return "Investment Assets amount cannot be zero."

# Cash Distribution
def calculate_cash_dist(investment_assets, cash, annual_gross_income):
    try:
        cash_dist = (cash / (investment_assets + cash + annual_gross_income)) * 100
        return round(cash_dist, 2)
    except ZeroDivisionError:
        return "Cash amount cannot be zero."

# Annual Gross Income Distribution
def calculate_annual_gross_income_dist(investment_assets, cash, annual_gross_income):
    try:
        annual_gross_income_dist = (annual_gross_income / (investment_assets + cash + annual_gross_income)) * 100
        return round(annual_gross_income_dist, 2)
    except ZeroDivisionError:
        return "Annual Gross Income amount cannot be zero."
      
# Investment Assets to Gross Pay Ratio Route HTML
@app.route("/iagpr/", methods = ["GET", "POST"])
def iagpr():
    if request.method == "POST":
        investment_assets = float(request.form["investment_assets"])
        cash = float(request.form["cash"])
        annual_gross_income = float(request.form["annual_gross_income"])
        iagpr = calculate_iagpr(investment_assets, cash, annual_gross_income)

        # Investment Assets to Gross Pay Ratio %Distribution
        investment_assets_dist = calculate_investment_assets_dist(investment_assets, cash, annual_gross_income)
        cash_dist = calculate_cash_dist(investment_assets, cash, annual_gross_income)
        annual_gross_income_dist = calculate_annual_gross_income_dist(investment_assets, cash, annual_gross_income)

        # Format IAGPR to Local Currency
        formatted_formia = locale.currency(investment_assets, grouping=True)
        formatted_formc = locale.currency(cash, grouping=True)
        formatted_formagi = locale.currency(annual_gross_income, grouping=True)
        return render_template("iagpr.html", iagpr = iagpr, 
                               investment_assets = formatted_formia, 
                               cash = formatted_formc, 
                               annual_gross_income = formatted_formagi,
                               investment_assets_dist = investment_assets_dist,
                               cash_dist = cash_dist,
                               annual_gross_income_dist = annual_gross_income_dist
                               )
    return render_template("iagpr.html", iagpr = None)
#--------------------------End Investment Assets to Gross Pay Ratio Page------------------------

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)