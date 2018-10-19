import sqlite3
def intialize():
	connection = sqlite3.connect('app.db')
	crsr = connection.cursor()
	sql_command = """CREATE TABLE users (  
	name VARCHAR(40),
	address VARCHAR(40),
	email VARCHAR(40),
	mobile_number VARCHAR(20) PRIMARY KEY,
	emergency_mobile_number VARCHAR(20);"""
	crsr.execute(sql_command)

	sql_command = """CREATE TABLE affected_people (  
	lat DECIMAL(10,8),
	lng DECIMAL(11,8),
	mobile_number VARCHAR(20) PRIMARY KEY,
	number_of_persons INTEGER;"""
	crsr.execute(sql_command)

	connection.commit()
	connection.close()

def insert(table_name, **kwargs):
    #something
    attributes=""
    values=""
    for key in kwargs:
    	attributes=attributes+key+","
    	values=values+kwargs[key]+","
    attributes=attributes[:-1]
    values=values[:-1]

    
    return

def get_emergency_contact(mobile_number):
    conn = sqlite3.connect('app.db')
    cursor = conn.execute("SELECT emergency_contact FROM users WHERE mobile_number = %s" %mobile_number)
    for row in cursor:
        emergency_contact = row[0]
    conn.close()
    return emergency_contact
    
def get_name_location(mobile_number):
    conn = sqlite3.connect('app.db') 
    cursor = conn.execute("SELECT name, address FROM users WHERE mobile_number = %s" %mobile_number)
    result = "Your Friend "
    for row in cursor:
        result = result + "Name: " + row[0]
        result = result + " M.No. " + mobile_number
    
    result += "Is struck at :"

    cursor = conn.execute("SELECT lattitude, longitude FROM affected_people WHERE mobile_number = %s" %mobile_number)
    
    for row in cursor:
        result = result + " location " + row[0] + ":" + row[1]
    
    return result

    
