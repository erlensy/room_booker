from roomBooker import bookRoom 
from datetime import timedelta
from datetime import date

def dateToString(date):
    return date.strftime("%Y-%m-%d")

bookingData = {
    "username" : "",
    "password" : "",
    "bookingText" : "kollokvie"
}

# monday = 0, tuesday = 1, wednesday = 2, thursday = 3
# friday = 4, saturday = 5, sunday = 6
bookings = [[0, "08:00", "12:00"],
            [1, "08:00", "12:00"],
            [2, "12:00", "16:00"],
            [3, "12:00", "16:00"],
            [4, "10:00", "14:00"]]

def bookBookings(startDate):
    currDate = startDate
    for booking in bookings:
        bookingDate, startTime, endTime = booking

        while currDate.weekday() != bookingDate:
            currDate += timedelta(1)

        currDateString = dateToString(currDate)

        try:
            bookRoom(bookingData["username"], bookingData["password"], 
                    startTime, endTime, currDateString,
                    bookingData["bookingText"])
            print(f"Booked rom on {currDateString}, from {startTime} to {endTime}")

        except:
            print(f"could not book room on {currDateString}, from {startTime} to {endTime}")

if __name__ == "__main__":
    disDate = date.today()
    for i in range(2):
        while disDate.weekday() != bookings[0][0]:
            disDate += timedelta(1)
        bookBookings(disDate)
        disDate += timedelta(1)
