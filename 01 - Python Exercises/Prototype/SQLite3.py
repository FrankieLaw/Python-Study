import sqlite3

con = sqlite3.connect("database/call_center_database.db")

def sql_fetch(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name from sqlite_master where type='table'")
    #cursorObj.execute( "SELECT * FROM customer LIMIT 4" )

    result = cursorObj.fetchall( )

    for row in result:
        print( row )

sql_fetch(con)