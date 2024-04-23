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

    commands = (
        """
        SELECT * 
        FROM cities 
        WHERE city='Northfield';
        """,
        '''
        SELECT city 
        FROM cities 
        WHERE pop = (SELECT MAX(pop) FROM cities);
        ''',
        '''
        SELECT city
        FROM cities
        WHERE pop = (SELECT MIN(pop) FROM cities WHERE state = 'Minnesota');
        ''',
        '''
        SELECT city
FROM cities
WHERE (lat, lon) IN (
    SELECT lat, lon FROM cities WHERE lat = (SELECT MAX(lat) FROM cities) UNION
    SELECT lat, lon FROM cities WHERE lon = (SELECT MAX(lon) FROM cities) UNION
    SELECT lat, lon FROM cities WHERE lat = (SELECT MIN(lat) FROM cities) UNION
    SELECT lat, lon FROM cities WHERE lon = (SELECT MIN(lon) FROM cities)
);

        '''
        )
    cur.execute(commands[0])

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

    cur.execute(commands[1])
    max_pop = cur.fetchall()
    print(max_pop[0])
    
    cur.execute(commands[2])
    min_pop_in_mn = cur.fetchall()
    print(min_pop_in_mn[0])

    cur.execute(commands[3])
    nsew = cur.fetchall()
    print(nsew[0, 1, 2, 3])


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



#Often we want to put a Python variable into an SQL query
def test_query_variable():
    
    # You will need to change the Port and the Password to use this code

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mlepinski",
        user="mlepinski",
        password="MyDatabasePassword")

    cur = conn.cursor()


    # Here the %s signals that we will replace this with a variable later
    sql = "SELECT name, abb FROM states WHERE abb = %s OR abb = %s "

    state_abb1 = 'MN'
    state_abb2 = 'NM'
    
    cur.execute( sql, [state_abb1, state_abb2]  )

    # IMPORTANT: We need a list of values for the second input to execute
    #   ... Even if we are only inserting my variable, it must be in a list
    # For example,  [state_abb1]
    
    row_list = cur.fetchall()

    for row in row_list:
        print(row)

    return None