import sqlite3
def insert(table_name, **kargs):
    #something
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