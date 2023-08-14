import gspread
from google.oauth2.service_account import Credentials
from email_sender import send_email
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# sets what im authorized to use with google cloud services
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# get the credentials from the config var
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# open the google sheets for mega bingo
SHEET = GSPREAD_CLIENT.open("mega-bingo")

# get the bingo book sheet
bingo_book_sheet = SHEET.worksheet("bingo-book")
# gets the numbers called sheet
numbers_called_sheet = SHEET.worksheet("numbers-called")

def create_bingo_book():
    """generates the numbers for the bingo book then appends them to the bingo book sheet in google sheets"""
    # creates a list of 90 numbers
    book_numbers = list(range(1,91))
    # list of lists of numbers for each row of the bingo book sheet and spaces
    book_rows_list = []

    # Sort the numbers into groups of 10 e.g. 1-10 ,11-20
    grouped_numbers = [book_numbers[i:i+10] for i in range(0, len(book_numbers), 10)]

    # Shuffle the numbers within each group and adds 8 spaces to each group before shuffling
    for group in grouped_numbers:
        empty_strings = [""] * 8
        group.extend(empty_strings)
        random.shuffle(group)

    # Iterate through each index of the list of numbers and creates a new list that match the rows so 
    # first number will be between 1-10 second will be between 11-20 and so on so then first column numbers will be 1-10 second 11-20
    for index in range(18):
       book_rows_list.append([group[index] for group in grouped_numbers])

    # adds the name and book id to first row
    book_rows_list.insert(0,["Mega Bingo\nBook ID: 123"])
    
    # this adds the list of empty strings to match the merged rows after every 3 rows in the bingo book
    for index in [4, 8, 12,16,20]:      
        book_rows_list.insert(index,[""] * 7 )
        
    # this appends the rows to the bingo book in google sheets
    #bingo_book_sheet.append_rows(book_rows_list)
    pdf_buffer = create_pdf(book_rows_list)
    send_email("GIFTSFORYOU83@GMAIL.COM","bingobook.pdf", pdf_buffer)

       
def create_pdf(row_list):   
    """creates a bingo book pdf with the numberers generated and calls email_sender 
    to send the pdf as attachment in an email to the users email"""

    # store pdf created in bytes
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