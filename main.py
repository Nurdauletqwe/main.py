import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_tables():
        cursor.execute('CREATE TABLE IF NOT EXISTS cinema (id INTEGER PRIMARY KEY, name TEXT, address TEXT)')
        cursor.execute('CREATE TABLE IF NOT EXISTS movie (id INTEGER PRIMARY KEY, name TEXT, genre TEXT, year INTEGER,  description TEXT, rating REAL)')
        cursor.execute('CREATE TABLE IF NOT EXISTS afisha (id INTEGER PRIMARY KEY, movie_id INTEGER, cinema_id INTEGER, price INTEGER, date DATE, time TIME, capacity INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS place (id INTEGER PRIMARY KEY, afisha_id INTEGER, room INTEGER, row INTEGER, seat INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS ticket (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, place_id INTEGER)')

create_tables()
conn.commit()

def get_movies():
    cursor.execute("SELECT id, name, genre, year FROM movie")
    movies = cursor.fetchall()
    return movies

def get_movie_table(movie_id):
    cursor.execute("SELECT id, cinema_id, price, date, time FROM afisha WHERE movie_id=?", (movie_id,))
    schedule = cursor.fetchall()
    return schedule

def get_available_seats(afisha_id):
    cursor.execute("SELECT id, room, row, seat FROM place WHERE afisha_id=? AND id NOT IN (SELECT place_id FROM ticket)", (afisha_id,))
    seats = cursor.fetchall()
    return seats

def book_ticket(name, phone, place_id):
    cursor.execute("INSERT INTO ticket (name, phone, place_id) VALUES (?, ?, ?)", (name, phone, place_id))
    conn.commit()

movies = get_movies()
print("Available movies:")
for movie in movies:
    print(movie)

def display_table(schedule):
    print("Available showtimes:")
    for index, session in enumerate(schedule, start=1):
        cinema_id = session[1]
        cursor.execute("SELECT name, address FROM cinema WHERE id=?", (cinema_id,))
        cinema_info = cursor.fetchone()
        cinema_name, cinema_address = cinema_info[0], cinema_info[1]
        print(f"{index}. Cinema: {cinema_name}, Address: {cinema_address}, Date: {session[3]}, Time: {session[4]}")

def select_movie_table():
    movies = get_movies()
    print("Available movies:")
    for movie in movies:
        print(f"{movie[0]}. {movie[1]} ({movie[2]}, {movie[3]})")

    movie_id = int(input("Select movie ID(between 1 to 100): "))
    table = get_movie_table(movie_id)
    display_table(table)

    afisha_id = int(input("Select session ID(example: 1): "))
    return afisha_id

def davailable_seats(seats):
    print("Available seats:")
    for seat in seats:
        print(f"Room: {seat[1]}, Row: {seat[2]}, Seat: {seat[3]}")

def book_ticket_buying():
    name = input("Enter your name(example: Nurdaulet): ")
    phone = int(input("Enter your phone number(example: 87007007070): "))
    afisha_id = select_movie_table()
    seats = get_available_seats(afisha_id)
    davailable_seats(seats)
    place_id = int(input("Select seat ID(example: 1): "))
    book_ticket(name, phone, place_id)
    print("Ticket booked successfully!")

book_ticket_buying()

def cancel_booking(ticket_id):
    cursor.execute('''DELETE FROM ticket WHERE id = ?''', (ticket_id,))
    conn.commit()
    print(f"Booking with ticket ID {ticket_id} has been cancelled.")

def book_ticket_buying():
    name = input("Enter your name(example: Nurdaulet): ")
    phone = int(input("Enter your phone number(example: 87007007070): "))
    afisha_id = select_movie_table()
    seats = get_available_seats(afisha_id)
    davailable_seats(seats)
    place_id = int(input("Select seat ID(example: 1): "))
    book_ticket(name, phone, place_id)
    print("Ticket booked successfully!")

def main():
    print("Welcome to Cinema Booking System!")
    print("1. Show Movies")
    print("2. Book Ticket")
    print("3. Cancel Booking")
    print("4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        select_movie_table()
    elif choice == "2":
        book_ticket_buying()
    elif choice == "3":
        ticket_id = int(input("Enter ticket ID to cancel booking: "))
        cancel_booking(ticket_id)
    elif choice == "4":
        exit()
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
