class Star_Cinema:
    __hall_list = []

    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    

    def entry_hall(self):
        Star_Cinema.__hall_list.append(self)
    

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__(rows, cols, hall_no)
        self._seats ={}
        self._show_list = []
        self.entry_hall()

    
    def entry_show(self, id, movie_name, time):
        if id not in self._seats:
            seat_matrix = []
            for i in range(self.rows):
                seat_row = [0] * self.cols
                seat_matrix.append(seat_row)
            self._seats[id] = seat_matrix
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        
    def book_seats(self, id, s_to_book):
        if id not in self._seats:
            raise ValueError("Invalid show ID.")

        seat_matrix = self._seats[id]

        for row, col in s_to_book:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if seat_matrix[row][col] == 0:
                    seat_matrix[row][col] = 1  # Mark as booked
                else:
                    raise ValueError(f"Seat ({row}, {col}) is already booked.")
            else:
                raise ValueError("Invalid seat. Not present in Hall")

    def view_show_list(self):
        show_list_str = ""
        for show in self._show_list:
            show_list_str += f"ID: {show[0]}        Movie Name: {show[1]}      Time: {show[2]}\n"
        return show_list_str 
        
    def view_available_seats(self, id):
        print(f"for {id}:\n")
        if id in self._seats:
            seat_matrix = self._seats[id]
            for row in seat_matrix:
                print(' '.join(map(str, row)))
        else:
            raise ValueError("Wrong ID")
        
def book_seats_interactively(hall):
    try:
        show_id = int(input("Enter the show ID to book seats: available show ID '111' or '222':  "))
        if show_id not in hall._seats:
            print("Invalid show ID.")
            return

        num_seats = int(input("Enter the number of seats to book: "))
        seats_to_book = []

        for i in range(num_seats):
            row = int(input(f"Enter the row number: between 0 to {hall.rows-1}: "))
            col = int(input(f"Enter the column number: between 0 to {hall.cols-1}: "))
            seats_to_book.append((row, col))

        hall.book_seats(show_id, seats_to_book)
        print("Seats booked successfully.")
        print(hall.view_available_seats(show_id))
    except ValueError as e:
        print(e)

def avaiable_seat(hall):
    id= int(input("Enter the show ID: available show ID '111' or '222':  "))
    print(hall.view_available_seats(id))

def Show_list(hall):
    show_list_hall = hall.view_show_list()
    return show_list_hall
        
# Usage
hall1 = Hall(4, 4, 1)
hall2 = Hall(5, 5, 2)

hall1.entry_show(111, "Jailer", "11:00 AM")
hall1.entry_show(222, "jawan", "2:00 PM")
hall2.entry_show(111, "leo", "12:00 PM")
hall2.entry_show(222, "bahubali", "3:00 PM")


while(True):
    op=int(input(" 1. List of Show\n 2. available Seat\n 3. Book Seat\n 4. exit\n Enter Option: "))
    if op==1:
        hall= int(input(" 1. Hall No 1\n 2. Hall No 2\n Enter Option: "))
        if hall ==1:
            print("Show list for Hall 1: ")
            print(Show_list(hall1))
        elif hall ==2:
            print("Show list for Hall 2: ")
            print(Show_list(hall2))
        else:
            raise ValueError("No More Hall available")
    elif op== 2:
        hall = int(input(" 1. available seat on Hall No 1\n 2. available seat on Hall No 2\n Enter Option: "))
        if hall ==1:
            print("Show available seat for Hall 1: ")
            avaiable_seat(hall1)
        elif hall ==2:
            print("Show available seat for Hall 2: ")
            avaiable_seat(hall2)
        else:
            raise ValueError("No More Hall available")
    elif op==3:
        hall = int(input(" 1. Hall No 1\n 2. Hall No 2\n Enter Option: "))
        if hall ==1:
            print("Booking for Hall 1:")
            book_seats_interactively(hall1)
        elif hall ==2:
            print("Booking for Hall 2:")
            book_seats_interactively(hall2)
        else:
            raise ValueError("No More Hall available")
    elif op == 4:
        break
            
            
    
