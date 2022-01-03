from roomBooker import bookRoom 
from datetime import timedelta
from datetime import date

def dateToString(date):
    return date.strftime("%Y-%m-%d")

def bookBookings(startDate):
    currDate = startDate
    for booking in bookings:
        bookingDate, roomId, startTime, endTime = booking

        while currDate.weekday() != bookingDate:
            currDate += timedelta(1)

        currDateString = dateToString(currDate)

        try:
            bookRoom(bookingData["username"], bookingData["password"], 
                    startTime, endTime, currDateString,
                    bookingData["bookingText"], roomIds[roomId])
            print(f"Booked room: {roomId} on {currDateString}, from {startTime} to {endTime}")

        except:
            print(f"Could not book room: {roomId} on {currDateString}, from {startTime} to {endTime}")

bookingData = {
    "username" : "",
    "password" : "",
    "bookingText" : "kollokvie"
}

roomIds = {
    "E404" : "341E404",
    "F404" : "341F404",
    "E304" : "341E304",
    "H415" : "301415",
    "R41" : "360D1-150",
    "R40" : "360D1-148",
    "R50" : "360A2-145",
    "R81" : "360D5-137",
    "R21" : "360AU2-101"
}

# monday = 0, tuesday = 1, wednesday = 2, thursday = 3
# friday = 4, saturday = 5, sunday = 6
bookings = [[0, "R41", "08:00", "12:00"],
            [1, "R41", "08:00", "12:00"],
            [2, "E404", "12:00", "16:00"],
            [3, "R41", "12:00", "16:00"],
            [4, "R41", "10:00", "14:00"]]

if __name__ == "__main__":
    disDate = date.today()
    for i in range(2):
        while disDate.weekday() != bookings[0][0]:
            disDate += timedelta(1)
        bookBookings(disDate)
        disDate += timedelta(1)
