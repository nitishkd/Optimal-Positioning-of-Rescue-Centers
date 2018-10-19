import sqlite3
conn = sqlite3.connect('app.db')
def insert(table_name, **kargs):
    #something
    return

def get_emergency_contact(mobile_number):
    cur = conn.cursor()
    emergency_contact = cur.execute("SELECT emergency_contact FROM users WHERE mobile_number = %s" %mobile_number)
    return emergency_contact
    