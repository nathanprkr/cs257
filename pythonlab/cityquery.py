'''
Determine if Northfield is present in the database. 
If it is, print its location (Latitude and Longitude). 
If it is not, print an appropriate message for the user.

Print out the name of the city with the largest population.

Print out the name of the city in Minnesota with the smallest population.

Print out the names of the cities that is furthest North, furthest East, 
furthest South, and furthest West

Have the user enter a State from the keyboard. Print the Total population of 
all the cities in that state. The user should be able to enter either an 
abbreviation or the full name of the sate. If the user enters an abbreviation, 
then you should look up the abbreviation in the second table to learn the full 
name of the state.
'''
import psycopg2

def query():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="parkern2",
        user="parkern2",
        password="python336spam")
    
    cur = conn.cursor()

    command = (
        """
        SELECT * FROM cities WHERE city='Northfield';
        """
        )
    cur.execute(command)

    row_list = cur.fetchall()

    if row_list == []:
        print("no cities match that name")

    else:
        for row in row_list:
            if row is None:
                print("There is no city that matches that name")

            else:
                print("the cities latitude is: " + row[3])
                print("the cities longitude is: " + row[4])


query()

def test_query_all():

    # You will need to change the Password to use this code
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mlepinski",
        user="mlepinski",
        password="MyDatabasePassword")

    cur = conn.cursor()

    sql = "SELECT name, abb FROM states"
    
    cur.execute( sql )

    # fetchall() returns a list containing all rows that matches your query
    row_list = cur.fetchall()

    # It is often useful to loop through all rows in a query result
    for row in row_list:
        print( row[1] )
    
    # Note: We could access individual items in the row
    # That is, row[0] would be the name column in the previous example
    #   ... and row[1] would be the abb column

    # Here I am leaving out the conn.commit() because we aren't changing
    #    either the database or the data in the database
    
    return None
