from Utilities import excel_utils


file = "C:\\Users\\Gowrishankar\\OneDrive\\Desktop\\myfile.xlsx"

# Writing data
excel_utils.write_data(file,"Sheet1", 1,1,"Name")
excel_utils.write_data(file,"Sheet1", 1,2,"Age")
excel_utils.write_data(file,"Sheet1", 1,3,"ID")

excel_utils.write_data(file,"Sheet1", 2,1,"Jack")
excel_utils.write_data(file,"Sheet1", 2,2,"26")
excel_utils.write_data(file,"Sheet1", 2,3,"001")


#fetching rows and columns number
print(excel_utils.get_row_count(file,"Sheet1"))#2
print(excel_utils.get_column_count(file,"Sheet1"))#3

#fill green and red colour in cell
excel_utils.fill_red(file, "Sheet1", 1,1)
excel_utils.fill_green(file,"Sheet1",1,2)

#reading data
print(excel_utils.read_data(file,"Sheet1", 1,1))
print(excel_utils.read_data(file,"Sheet1", 1,2))
print(excel_utils.read_data(file,"Sheet1", 1,3))
print(excel_utils.read_data(file,"Sheet1", 2,1))
print(excel_utils.read_data(file,"Sheet1", 2,2))
print(excel_utils.read_data(file,"Sheet1", 2,3))

