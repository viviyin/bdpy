import sqlite3
import time

connection1 = sqlite3.connect('data/demo102.sqlite.db')
print("sqlite3 connect successfully")

emp1 = {'NAME': 'Mark', 'AGE': 43, 'DEPT': 1, 'ADDR': 'Taipei'}
emp2 = {'NAME': 'John', 'AGE': 43, 'DEPT': 2, 'ADDR': 'Hsinchu'}
emp3 = {'NAME': 'Ken', 'AGE': 44, 'DEPT': 3, 'ADDR': 'Taipei'}
emp4 = {'NAME': 'Tim', 'AGE': 45, 'DEPT': 2, 'ADDR': 'Hsinchu'}

employees = [emp1, emp2, emp3, emp4]
sql_dml = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES(?,?,?,?)"

start_time = time.time()
for i in range(1000):
    for e in employees:
        connection1.execute(sql_dml, (e['NAME'], e['AGE'], e['DEPT'], e['ADDR']))
        connection1.commit() # 12.818
    # connection1.commit() # 3.2699
#connection1.commit() # 4008
end_time = time.time()
connection1.close()
print(f"total time ={end_time - start_time}")
