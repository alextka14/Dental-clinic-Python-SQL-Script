import sqlanydb


def connect_to_database(uid='dba', pwd='sql', host='srv-dental.demos.local:2638'):
    return sqlanydb.connect(uid=uid, pwd=pwd, host=host)


def execute_query(cursor, query, parameters=None):
    cursor.execute(query, parameters)


def get_patient_name(cursor, patient_id):
    query = """SELECT surname, firstname, middlename FROM patients WHERE patient_id = CONVERT(char, ?)"""
    cursor.execute(query, (patient_id,))
    result = cursor.fetchone()

    if result:
        return ' '.join(map(str, result))
    else:
        return ''


def write_to_file(file_path, data, get_name_function):
    with open(file_path, 'w') as file:
        for time, patient_id in data:
            full_name = get_name_function(patient_id)
            file.write(f':{time};<{full_name}>\n' if full_name else f':{time};<Никого>\n')


def main():
    conn = connect_to_database()
    curs = conn.cursor()
    curs2 = conn.cursor()
    curs3 = conn.cursor()
    curs4 = conn.cursor()

    queries = [
        """SELECT "start", pat_id FROM a_appointments 
        WHERE day(app_date) = day(getdate()) AND 
        month(app_date) = month(getdate()) AND 
        year(app_date) = year(getdate()) AND 
        "start" BETWEEN '8:00' AND '22:00' AND 
        app_book_id = 1""",
        """SELECT "start", pat_id FROM a_appointments 
        WHERE day(app_date) = day(getdate()) AND 
        month(app_date) = month(getdate()) AND 
        year(app_date) = year(getdate()) AND 
        "start" BETWEEN '8:00' AND '22:00' AND 
        app_book_id = 131"""
    ]

    for i, query in enumerate(queries, start=1):
        execute_query(curs, query)
        data = [(str(row[0]), str(row[1])) for row in curs.fetchall()]
        write_to_file(f'C://py_scripts/{i}.txt', data, lambda patient_id: get_patient_name(curs2, patient_id))

    curs.close()
    curs2.close()
    curs3.close()
    curs4.close()
    conn.close()


if __name__ == "__main__":
    main()
