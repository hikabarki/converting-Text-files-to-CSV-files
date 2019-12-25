import xlwt
import glob
import operator

# Create a workbook object
wb = xlwt.Workbook()
# # Add a sheet object
ws = wb.add_sheet('Sheet8',cell_overwrite_ok=True)
rowy = 0

for text_filename in glob.glob('*.txt'):
    with open(text_filename) as f_input:
        try:
            lines = [line.strip() for line in operator.itemgetter(0,1,2,3,4,5)(f_input.readlines())]
        except IndexError as e:
            print ("'{}' is too short".format(text_filename))
            lines = []

    # Output to Excel sheet
    for colno, colitem in enumerate(lines):
        ws.write(rowy, colno, colitem)

    rowy += 1

# Write the output file.
wb.save('output.xls')