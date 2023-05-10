import csv

def compared_csv_files(file1,file2, output_file):
    with open(file1,'r',newline='') as csv_file1, \
        open(file2,'r', newline='') as csv_file2, \
        open(output_file, 'w', newline='') as output_csv_file:
    
        reader1 = csv.reader(csv_file1)
        reader2 = csv.reader(csv_file2)
        writer = csv.writer(output_csv_file, delimiter='\t')

        #парсер первого файла и занесение его элементов в лист для дальнейшей обработки
        arr_File_keys = []
        for row1 in reader1:
            index_row = row1[0].find(';')
            arr_File_keys.append(row1[0][index_row+1:])
        arr_File_keys.pop(0)
        compared_row = []

        for row2 in reader2:
            #парсер второго файла строчек, чтобы остались только "groupname"
            groupname = row2[0]
            index_row = groupname.find(';') + 1
            groupname = groupname[index_row:]
            index_row2 = groupname.find(';')
            groupname = groupname[:index_row2]
            
            found_ip = search_ip_file1(arr_File_keys, groupname) 
            found_ip = found_ip + ';'  if found_ip != '' else ''

            out_line = row2[0][:index_row] + found_ip + row2[0][index_row:]

            compared_row.append(out_line)
        writer.writerows(compared_row)

def search_ip_file1(arr_File_keys, groupname): #поиск "ip" по "groupname" 
    for line_file1 in arr_File_keys:
        index_row = line_file1.find(';')
        str_id = line_file1[:index_row]
        if groupname in line_file1:
            return str_id
    return ''


file1 ='./Task_3_Excel_File/ExcelFile1.csv'
file2 ='./Task_3_Excel_File/ExcelFile2.csv'
output_file = './OutExcelFileTask3.csv'

compared_csv_files(file1, file2, output_file)