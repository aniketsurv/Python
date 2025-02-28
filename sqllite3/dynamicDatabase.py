import json
import sqlite3



def insertobjinDB(con,obj,table_name):
    print("obj--->",obj)
    # Insert multiple rows
    #command = "INSERT INTO todo (id, task, date, status) VALUES (?, ?, ?, ?)"
    
    # Extract the columns and values from the object
    columns = ', '.join(obj.keys())
    placeholders = ', '.join(['?'] * len(obj))
    values = tuple(obj.values())
    
    # Create the INSERT INTO statement dynamically
    command = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    
    print("commanddddd---->", command)
    
    # Execute the command
    con.execute(command, values)
    con.commit()
    print(f"Values inserted into table '{table_name}': {obj}")

#Dynamic table creation
def create_tables(db_name,obj):
        with open("db_schema.json") as f:
            data = json.load(f)
            con = sqlite3.connect(db_name+".db")
            list(con.execute('pragma foreign_keys = on'))
            sqlite_cursor = con.cursor()
            
            for table_name, columns in data.items():
                print(table_name , columns)
                
                #Generate the CREATE TABLE statement dynamically
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
                column_definitions = []
                unique_constraints = []
                
                for column_name, properties in columns.items():
                    if column_name != "UNIQUE":
                        column_definitions.append(f"{column_name} {properties['type']}")
                    else:
                        # Handling unique constraints
                        unique_constraints = [col_name for col_name in properties.keys()]
                
                create_table_query += ", ".join(column_definitions)
                
                if unique_constraints:
                    create_table_query += ", UNIQUE (" + ", ".join(unique_constraints) + ")"
                
                create_table_query += ")"
                
                # Execute the CREATE TABLE statement
                sqlite_cursor.execute(create_table_query)
                print(f"Table '{table_name}' successfully created.")
                
                insertobjinDB(con,obj,table_name)

obj ={
        "PLAY_LIST_ID":"123456789",
        "TRACK_COUNT":"1",
        "PLAY_LIST_NAME":"2.04.5",
        "version":"25",
        "entity_type": "Device",
        "KEY_VAL": "kjredfnjresefnffmdj;ajd d;55fdmdjs,l",
        "PLAYLIST_ALBUM_IMAGE_URI": "85jkdjkdnsd",
        "CML_HOUSEHOLD_ID": "fkjfdnfjdjsmsmsmsm",
        "syncComplete": "done",
}

with open("tablenames.json") as f:
            data = json.load(f)
            # print(data)
            for dbname in data.values():
                # print("name list-->",dbname)
                for t in dbname:
                    print("database_names-->",t)
                    create_tables(t,obj)
    