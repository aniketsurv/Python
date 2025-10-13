import sqlite3

#Check version
print(sqlite3.sqlite_version)

#used for connect and create database
conn = sqlite3.connect("test.db")
print("database created.")
  
# used for table creation
# command = "create table todo (id int,task text,date text,status text)"  
# conn.execute(command)
# print ("Table created successfully")

# #used for insert data
# command = "insert into todo (id, task, date, status) values (1, 'study SQLite3', '5-8-2024', 'Done')"  
# conn.execute(command)
# conn.commit()


# #insert multiple data
# # Define the data to be inserted
# tasks = [
#     (2, 'write Python script', '6-8-2024', 'Pending'),
#     (3, 'read documentation', '7-8-2024', 'In Progress'),
#     (4, 'attend meeting', '8-8-2024', 'Done'),
#     (5, 'review code', '9-8-2024', 'Pending')
# ]
# # Insert multiple rows
# command = "INSERT INTO todo (id, task, date, status) VALUES (?, ?, ?, ?)"
# conn.executemany(command, tasks)





# #Update data in table
# command = "update todo set status = 'done' where id = 2"  
# conn.execute(command)




# #Delete row in table
# command = "delete from todo where id = 1" 
# conn.execute(command)


#Delete table
# command = "drop table todo"
#conn.execute(command)


#fetch/retrive data in table
command = "select * from todo"  
fetchObj = conn.execute(command)
# for data in fetchObj:
#     print(data)
    
lst = fetchObj.fetchall()
print(lst)







# Commit the transaction used for change any value in table
conn.commit()


conn.close()



