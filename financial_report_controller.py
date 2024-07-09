from financial_entities import Text, Table , Report
from financial_data_gateway import FinancialDataGateway

class FinancialReportController:
    def __init__(self, report_generator):
        self.report_generator = report_generator

    def handle_request(self, request , accountId):
        report_data =''
        if request == "view_online":
            table_data_customer = Table(data=FinancialDataGateway("CUSTOMER_DATA.db").fetch_data("SELECT * FROM CUSTOMER_DATA where ACCOUNTID="+accountId))
            if table_data_customer.data:
                account_id,name, phone,entity = table_data_customer.data[0]

            table_data_trade = FinancialDataGateway("CUSTOMER_DATA.db").fetch_data("SELECT * FROM TRADE_DATA where ACCOUNTID="+accountId)
            report_data=Report(trades=table_data_trade,account_id=account_id,name=name, phone=phone,entity=entity)

        if request == "generate_pdf":
            text = Text(content=open("input.txt").read())
            table_data_customer = Table(data=FinancialDataGateway("CUSTOMER_DATA.db").fetch_data("SELECT * FROM CUSTOMER_DATA where ACCOUNTID="+accountId))
            if table_data_customer.data:
                ACCOUNTID,NAME, PHONE,ENTITY = table_data_customer.data[0]
                replacements = {
                "{ACCOUNTID}": ACCOUNTID,
                 "{NAME}": NAME,
                 "{PHONE}": PHONE,
                 "{ENTITY}":ENTITY
                }

                updated_content = text.replace_placeholders(replacements)
            table_data_trade = FinancialDataGateway("CUSTOMER_DATA.db").fetch_data("SELECT * FROM TRADE_DATA where ACCOUNTID="+accountId)
            self.report_generator.generate_report(updated_content, table_data_trade)

        return report_data