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
        WHERE lat = (SELECT MAX(lat) FROM cities);
        ''',
        '''
        SELECT city
        FROM cities
        WHERE lon = (SELECT MAX(lon) FROM cities);
        ''',
        '''
        SELECT city
        FROM cities
        WHERE lat = (SELECT MIN(lat) FROM cities);
        ''',
        '''
        SELECT city
        FROM cities
        WHERE lon = (SELECT MIN(lon) FROM cities);
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
    print("max population:", max_pop)
    
    cur.execute(commands[2])
    min_pop_in_mn = cur.fetchall()
    print("smallest pop in MN:", min_pop_in_mn)

    cur.execute(commands[3])
    north = cur.fetchall()
    cur.execute(commands[4])
    east = cur.fetchall()
    cur.execute(commands[5])
    south = cur.fetchall()
    cur.execute(commands[6])
    west = cur.fetchall()
    print("furthest north:", north)
    print("furthest east:", east)
    print("furthest south:", south)
    print("furthest west:", west)


    state_pop = """SELECT SUM(pop)
            FROM cities
            WHERE state = %s;"""
    
    code_lookup = """SELECT state 
            FROM states
            WHERE code = %s;"""

    inpt = str(input("what is the state name/abv?: "))

    if len(inpt) == 2:
        cur.execute(code_lookup, (inpt,))
        state = cur.fetchall()
        cur.execute(state_pop, state)
        total_pop = cur.fetchall()
        print("Total city population:", total_pop)
    elif len(inpt) > 2:
        cur.execute(state_pop, (inpt.capitalize(),))
        total_pop = cur.fetchall()
        print("Total city population:", total_pop)
    else:
        print("invalid input")
    
query()