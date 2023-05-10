import glob
import os

directory = './bar'
csv_files = glob.glob(directory + './**/*.csv', recursive=True)

for file in csv_files:#Вывод
    file_name = os.path.splitext(os.path.basename(file))[0]
    print(file_name) 