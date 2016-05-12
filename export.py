import xlsxwriter

def exportDailyStats(apiDaily, apiServices,name):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(name+'.xlsx')
    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 5)
    worksheet.set_column('C:C', 5)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('G:G', 5)
    worksheet.set_column('H:H', 5)
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Date', bold)
    worksheet.write('B1', 'Clicks', bold)
    worksheet.write('C1', 'Shares',bold)
    worksheet.write('F1', 'Service', bold)
    worksheet.write('G1', 'Clicks', bold)
    worksheet.write('H1', 'Shares', bold)

    rowNum = 2

    for item in apiDaily:
        for sub in item:
            if sub == 'date':
                worksheet.write('A'+str(rowNum), item[sub])
            elif sub == 'clicks':
                worksheet.write('B'+str(rowNum), item[sub])
            else:
                worksheet.write('C'+str(rowNum), item[sub])
        rowNum += 1
    
    rowNum = 2

    for item in apiServices:
        for sub in item:
            if sub == 'service':
                worksheet.write('F'+str(rowNum), item[sub])
            elif sub == 'clicks':
                worksheet.write('G'+str(rowNum), item[sub])
            elif sub == 'shares':
                worksheet.write('H'+str(rowNum), item[sub])
        rowNum += 1
    workbook.close()


