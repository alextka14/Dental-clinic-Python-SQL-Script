from datetime import datetime

# Определение текущего времени
current_time = datetime.now().strftime("%H:%M")[:-1] + '0'

# Список файлов входного и выходного файла
file_pairs = [
    ('C://py_scripts/1.txt', 'C://py_scripts/3.txt'),
    ('C://py_scripts/2.txt', 'C://py_scripts/4.txt')
]

# Функция для поиска пациента совпадающего по времени и записи его в файл
def find_matching_patient(input_file_path, output_file_path):
    # Чтение строк из входного файла
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Переменная для хранения данных перед записью в файл
    data_to_write = ""

    # Поиск совпадения по времени и запись данных
    for line in lines:
        time, patient_info = line.split(":")[1], line.split("<")[1].split(">")[0]
        if time.strip() == current_time and patient_info.strip() != 'Никого':
            data_to_write = line
            break

    # Запись данных в файл
    with open(output_file_path, 'w') as output_file:
        output_file.write(data_to_write)

# Обработка файлов с использованием цикла
for input_file_path, output_file_path in file_pairs:
    find_matching_patient(input_file_path, output_file_path)

# Чтение данных из файлов 3.txt и 4.txt
with open('C://py_scripts/3.txt', 'r') as txt3, open('C://py_scripts/4.txt', 'r') as txt4:
    patient_info_3 = txt3.readline().split(":")[1].strip()
    patient_info_4 = txt4.readline().split(":")[1].strip()

# Запись в файл
output_file_path_final = 'C://inetpub/wwwroot/patient/apachidi.php'
with open(output_file_path_final, 'w', encoding='utf-8') as txt5:
    txt5.write(f"""<html>
      <head>
        <meta charset="utf-8">
        <title>Таблица пациентов</title>
    	<link href="style.css" rel="stylesheet" type="text/css">
      </head>
      <body>
        <table>
    		<tr>
    		<td>
            <div align="center"><big><big><big><big><big><big><big><big>{patient_info_3}</big></big></big></big></big></big></big></big></div>
            </td>
            </tr>
            <tr>
    		<td>
            <div align="center"><big><big><big><big><big><big><big><big>{patient_info_4}</big></big></big></big></big></big></big></big></div>
            </td>
    		</tr>
    	</table>
      <br></br>
        <table>
    		<tr>
    		<td>
            <div align="center"><big><big><big><big><big><big><big><big>{patient_info_3}</big></big></big></big></big></big></big></big></div>
            </td>
            </tr>
            <tr>
    		<td>
            <div align="center"><big><big><big><big><big><big><big><big>{patient_info_4}</big></big></big></big></big></big></big></big></div>
            </td>
    		</tr>
    	</table>
        <?php
            header("Refresh: 20");
            ?>
      </body>
    </html>""")
