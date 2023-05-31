import sqlite3 as db
import pandas as pd
connection = None
cursor = None
Customer_tbl = """
    CREATE TABLE IF NOT EXISTS Customer(
    id integer primary key autoincrement,
    First_name TEXT,
    Sure_name Text,
    Pstcode TEXT,
    House_number INTEGER,
    Phone_number numeric
    )
"""

Bouncycastle_tbl = """
    CREATE TABLE IF NOT EXISTS Bouncycastle (
    id integer primary key autoincrement,
    name text,
    dimension INTEGER,
    main_colour TEXT,
    max_occupants INTEGER,
    hire_price INTEGER,
    booked_date TEXT


    )
"""

Booking_tbl = """
    CREATE TABLE IF NOT EXISTS Booking (
    id integer primary key autoincrement,
    Customer_id INTEGER,
    Castle_id  INTEGER,
    booking_date INTEGER,
    FOREIGN KEY (Customer_id) REFERENCES Customer(id) on DELETE CASCADE,
    FOREIGN KEY (Castle_id) REFERENCES Bouncycastle(id) on DELETE CASCADE
    )
"""

def add_booking(customer_id, booking_id, booking_date):
    statement="INSERT INTO Booking VALUES(NULL,?,?,?)"  
    cursor.execute(statement, (customer_id, booking_id, booking_date))
    connection.commit()

def view_bookings():
    statement="""
    select booking_date as 'Booking date', 
    First_name as 'first name', 
    Sure_name as 'surname', 
    Pstcode as 'postcode', 
    House_number as 'house number',  
    Phone_number as 'phone' 
    from Booking 
    JOIN customer on customer.id = booking.Customer_id
    """
    print(pd.read_sql_query(statement, connection ))
    

def add_Customer(first_name, surname, postcode, house_number, phone_number):
    statement="INSERT INTO Customer VALUES(NULL,?,?,?,?,?)"  
    success = cursor.execute(statement, (first_name, surname, postcode, house_number, phone_number))
    connection.commit()
    if success:
        print("Customer added!")
        result = cursor.fetchone()
        return result
    

def view_Customer():
    statement="SELECT * FROM Customer"
    print(pd.read_sql_query(statement, connection ))

def update_Customer(customer_id, first_name, surname, postcode, house_number, phone_number):
    statement="UPDATE Customer SET First_name=?, Sure_name=?, Pstcode=?, House_number=?, Phone_number=? WHERE id=?"
    cursor.execute(statement,(first_name, surname, postcode, house_number, phone_number, customer_id))
    connection.commit()

def delete_Customer(customer_id):
    statement="DELETE FROM Customer WHERE id=?"
    cursor.execute(statement, (customer_id,))
    connection.commit()



    "insert into Customer values"
def add_Bouncycastle(name, Dimension, main_colour, max_occupants, Hire_price, Booked_date):
    statement="INSERT INTO Bouncycastle (name, dimension, main_colour, max_occupants, hire_price, booked_date) VALUES(?,?,?,?,?,?)"  
    cursor.execute(statement, (name, Dimension, main_colour, max_occupants, Hire_price, Booked_date))
    connection.commit()

def view_Bouncycastle():
    statement="SELECT * FROM Bouncycastle"
    print(pd.read_sql_query(statement, connection ))

def update_Bouncycastle(Dimension, main_colour, name, max_occupants, Hire_price, Booked_date):
    statement="UPDATE Bouncycastle SET dimension=?, main_colour=?, name=?, max_occupants=?, hire_price=?, booked_date=? WHERE id=?"
    cursor.execute(statement,(Dimension, main_colour, name, max_occupants, Hire_price, Booked_date))
    connection.commit()

def delete_Customer(Bouncycastle):
    statement="DELETE FROM Bouncycastle WHERE id=?"
    cursor.execute(statement, (Bouncycastle,))
    connection.commit()





def main():
    global connection, cursor
    connection = db.connect("Castle.db")
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys=1')
    cursor.execute(Customer_tbl)
    cursor.execute(Bouncycastle_tbl)
    cursor.execute(Booking_tbl)
    print("Initialised database")
    print("------------")
    print("Customer list")
    view_Customer()
    print("bouncecastle list")
    view_Bouncycastle()
    # get the customer details
    add_c = input("add a customer? (y/n) ")
    if add_c=='y':
        f_name = input("First name? ")
        surname = input("Surname? ") 
        postcode = input("Customer postcode? ")
        age = input("Age? ")
        phone = input("Phone number? ")
        # add to database
        customer = add_Customer(f_name, surname, postcode, age, phone)
        print("customer details")
        print(customer)

 
    
    castle_name  = input("What is the castle name? ")

    add_Bouncycastle(castle_name, 16, "Blue", 12, 50, "10/05/2023")
    
    customer_id = 1
    Bouncycastle_id = 1
    Book_date = '10/05/2023'
    add_booking(customer_id,Bouncycastle_id,Book_date)
    view_bookings()




if __name__ == "__main__":
    main()
