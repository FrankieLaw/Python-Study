import sqlalchemy
engine = sqlalchemy.create_engine( "sqlite:///database/call_center_database.db" )

inspector = sqlalchemy.inspect( engine )
schemas = inspector.get_schema_names( )

'''
SQLAlchemy Version
'''
print( sqlalchemy.__version__ )


'''
    Getting all of the Tables inside of the Database
    And show all the columns inside of the Schema
'''
for schema in schemas:
    print( "DATABASE: %s" %schema )
    print( "\n" )

    for table_name in inspector.get_table_names( schema = schema ):
        print( "SCHEMA: "  + table_name )

        for column in inspector.get_columns( table_name, schema = schema ):
            print( "Column: %s" %column )

        print( "\n" )


'''
    Getting all of the Tables
'''
print( "ALL TABLE NAMES" )
print( inspector.get_table_names( ) )


'''
    Running Query
'''
print( "\n\n" )
print( "Running Query ================================ ")
print( "Running Query ================================ ")
print( "Running Query ================================ ")
print( "\n\n" )

database = 'customer'
columns = ["CustomerID, Name, Occupation, Age"]
'''
print( "==============================================" )
print( "\t".join(columns) )
print( "==============================================" )
'''
with engine.connect( ) as con:
    #rs = con.execute( 'SELECT * FROM agent' )
    #rs = con.execute( 'SELECT * FROM agent LIMIT 4' )
    #rs = con.execute( 'SELECT * FROM customer LIMIT 15' )
    #rs = con.execute( 'SELECT Name, occupation, email FROM customer LIMIT 15')
    #rs = con.execute( "SELECT " + " ".join(columns) + " FROM customer ORDER BY CAST(CustomerID AS Integer) DESC LIMIT 15 " )
    #rs = con.execute( "SELECT " + " ".join(columns) + " FROM customer WHERE Occupation='Student' LIMIT 15 " )
    #rs = con.execute( "SELECT * FROM Customer WHERE Name LIKE '%Mary%'" )
    #rs = con.execute( "SELECT customerID, name, occupation FROM customer Where Occupation !='Unemployed' Limit 15" )
    #rs = con.execute( "SELECT agent.AgentID, agent.Name, call.ProductSold, call.CallID FROM agent JOIN call ON agent.AgentID = call.AgentID ORDER BY agent.Name DESC LIMIT 50" )
   
    
    rs = con.execute( 
        """
            SELECT Age,
                CASE
                    WHEN Age >= 30 THEN 'Yes'
                    WHEN Age < 30 THEN 'No'
                    ELSE 'Missing Data'
                END AS AgeFlag
            FROM Customer
            ORDER BY Name DESC
        """
    )

    for row in rs:
        output = ""

        for item in row:
            output = output + str(item) + "\t"

            '''
            if( isinstance( item, int ) ):
                print( "it is an int" )
                output = output + str( item )
            else:
                output = output + item + " || "
            '''
        print( output )
        


'''
    rs = con.execute( 
        """
            SELECT CAST(Age as Integer),
                CASE
                    WHEN Age >= 30 THEN 'Yes'
                    WHEN Age < 30 THEN 'No'
                    ELSE 'Missing Data'
                END AS AgeFlag
            FROM Customer
            ORDER BY Name DESC
            LIMIT 20
        """
    )
    ''' 

'''
    rs = con.execute( 
        """
            SELECT CAST(Age AS TEXT),
                CASE
                    WHEN Age == '0' THEN 'No Text 0'
                    WHEN Age == 0 THEN 'NUMBER 0'
                    WHEN Age >= 30 THEN 'Yes Greater than 30'
                    WHEN Age < 30 THEN 'No Less than 30'
                    ELSE 'Missing Data'
                END AS AgeFlag
            FROM TestData
        """
    )
'''

'''
agentSchema = inspector.get_columns( database )
agentColumn = []

for column in agentSchema:
    agentColumn.append( column["name"] )
'''