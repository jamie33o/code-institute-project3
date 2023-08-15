"""this module is for creating a pdf from the data passed to the function"""
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



def bingo_book_to_pdf(row_list):   
    """creates a bingo book pdf with the row_list data  and returns it as bytes """

    # store pdf in bytes
    pdf_buffer = BytesIO()
    # Create a PDF document
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    elements = []
    
    # Create a grid table from row lists data
    table = Table(row_list)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.red),
        ("SPAN", (0,0), (8,0)),
        ("SPAN", (0,4), (8,4)),
        ("SPAN", (0,8), (8,8)),
        ("SPAN", (0,12), (8,12)),
        ("SPAN", (0,16), (8,16)),
        ("SPAN", (0,20), (8,20)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)
    
    # Build PDF
    doc.build(elements)
    return pdf_buffer