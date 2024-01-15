from io import BytesIO
import xlsxwriter
from .models import Item

def generate_inventory_report():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    header_format = workbook.add_format({
        'bg_color': '#808080', 
        'bold':True, 
        'font_color':'white', 
        'align':'center',
        'border':1,
    })
    content_format = workbook.add_format({
        'border':1
    })
    worksheet = workbook.add_worksheet()
    worksheet.freeze_panes(1, 0)
    worksheet.write('A1', 'Item Name', header_format)
    worksheet.write('B1', 'Item Price', header_format)
    worksheet.write('C1', 'Unit Per Item', header_format)
    worksheet.write('D1', 'Unit Price', header_format)
    worksheet.write('E1', 'Description', header_format)
    model_obj = Item.objects.all()
    row = 2
    for qobj in model_obj:
        worksheet.write('A'+str(row), qobj.item_name, content_format)
        worksheet.write('B'+str(row), qobj.item_price, content_format)
        worksheet.write('C'+str(row), qobj.unit_per_item, content_format)
        worksheet.write('D'+str(row), qobj.unit_price(), content_format)
        worksheet.write('E'+str(row), qobj.description, content_format)
        row += 1

    worksheet.autofit()
    workbook.close()
    return output
