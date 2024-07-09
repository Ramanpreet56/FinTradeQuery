from flask import Flask, request, jsonify, render_template
from financial_report_controller import FinancialReportController
from financial_report_generator import FinancialReportGenerator

app = Flask(__name__)
report_generator = FinancialReportGenerator("output.pdf")
report_controller = FinancialReportController(report_generator)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/view_online', methods=['POST'])
def generate_report():
    accountId = request.form['accountId']
    report_content=report_controller.handle_request("view_online",accountId)
    account_id = report_content.account_id
    name = report_content.name
    phone = report_content.phone
    entity = report_content.entity
    trades = report_content.trades 
    return render_template('view_online.html', account_id=account_id, name=name, phone=phone, entity=entity, trades=trades)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    accountId = request.form['accountId']
    report_controller.handle_request("generate_pdf",accountId)
    return render_template('base.html', message='Report generated successfully and is available to download')

if __name__ == '__main__':
    app.run(debug=True)
