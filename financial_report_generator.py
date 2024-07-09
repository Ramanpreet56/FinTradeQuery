from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet
from financial_entities import Text, Table as FinancialTable  # Alias Table to avoid conflict
from reportlab.lib import colors

class FinancialReportGenerator:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate_report(self, text, table_data):
        doc = SimpleDocTemplate(self.output_path, pagesize=letter)
        styles = getSampleStyleSheet()

        if isinstance(text, str):
            text = Paragraph(text, styles['Normal'])
        flowables = [text]

        if isinstance(table_data, (list, tuple)) and len(table_data) > 0:
            table_header = ['TRADEID','ACCOUNTID','ENTITY','PORTFOLIO','COUNTERPART','TRADE DATE','STATUS'] 
            table_data_formatted = [table_header] + list(table_data) 
            table_style = [
                ('GRID', (0, 0), (-1, -1), 1, colors.black),  
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),  
            ]
            
            table = Table(table_data_formatted, style=table_style)
            flowables.append(table)

        doc.build(flowables)
