from openpyxl import Workbook
from openpyxl.styles import Font

def creandoExcel():
    
    #iniciando las librerias para crear excel
    
    book = Workbook()
    
    #activar la edicion de columnas
    
    sheet = book.active
    
    #seleccionar las columnas
    sheet['A1'] ="ID"
    sheet['B1'] ="Username"
    sheet['C1'] ="Password"
    sheet['D1'] ="CreationDate"
    
    sheet['A1'].font = Font(color='1D5D9B', bold=True)
    sheet['B1'].font = Font(color='1D5D9B', bold=True)
    sheet['C1'].font = Font(color='1D5D9B', bold=True)
    sheet['D1'].font = Font(color='1D5D9B', bold=True)
    
    book.save("bd_login.xlsx")
    
creandoExcel()