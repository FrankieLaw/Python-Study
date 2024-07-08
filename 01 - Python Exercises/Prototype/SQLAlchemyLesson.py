import sqlalchemy
engine = sqlalchemy.create_engine( "sqlite:///database/call_center_database.db" )

inspector = sqlalchemy.inspect( engine )
schemas = inspector.get_schema_names( )

'''
    Getting all of the Tables inside of the Database
    And show all the columns inside of the Schema
'''
for schema in schemas:
    print( "================================")
    print( "DATABASE: %s" %schema )
    print( "================================\n")
    for table_name in inspector.get_table_names( schema = schema ):
        print( "SCHEMA: "  + table_name )

        for column in inspector.get_columns( table_name, schema = schema ):
            print( "Column: %s" %column )

        print( "\n" )


'''
    Getting all of the Tables
'''
print( "================================")
print( "ALL TABLE NAMES" )
print( "================================")
print( inspector.get_table_names( ) )


'''
    Running Query
'''
print( "\n\n" )
print( "Running Query ================================")
with engine.connect( ) as con:
    rs = con.execute( "SELECT * FROM customer Limit 15" )

    for row in rs:
        print( "%s" %str(row) )

