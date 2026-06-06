ROOMS = {
    "101": {"type": "single", "rate": 80, "occupied": False},
    "102": {"type": "single", "rate": 80, "occupied": False},
    "201": {"type": "double", "rate": 120, "occupied": False},
    "202": {"type": "double", "rate": 120, "occupied": False},
    "301": {"type": "suite", "rate": 250, "occupied": False},
}

hotel = {
    "total_earned": 0,
    "guests": {}
}
name = ""
Room_num = 0

is_on = True
def book(type_of_room):
    global name
    global Room_num
    bill = 0
    for room in ROOMS:

        if not ROOMS[room]["occupied"] and ROOMS[room]["type"] == type_of_room:
            name = input("Please enter your name: ")
            nights = int(input("Please enter the number of nights you are staying: "))
            bill += ROOMS[room]["rate"] * nights
            hotel["guests"][room] = {
                "name": name,
                "nights": nights,
                "cost": bill
            }
            ROOMS[room]["occupied"] = True
            #hotel["total_earned"] += hotel["guests"][room]["cost"]
            return f"Room {room} booked for {name} for {nights}. Total {bill}"
    return f"Sorry, no {type_of_room} rooms available."



def checkout(room_to_checkout):
    if room_to_checkout not in ROOMS:
        return "Room does not exist."
    if not ROOMS[room_to_checkout]["occupied"]:
        return f"Room {room_to_checkout} is not currently occupied."
    else:
        guest = hotel["guests"][room_to_checkout]
        ROOMS[room_to_checkout]["occupied"] = False
        hotel["total_earned"] += guest["cost"]
        del hotel["guests"][room_to_checkout]
        return f"{guest['name']} has checked out. Bill: ${guest['cost']}. Thank you!"

def report(ROOMS):
    for room in ROOMS:

        if not ROOMS[room]["occupied"]:
            status = "Available"
        else:
            guest = hotel['guests'][room]
            #status = "Occupied by Alice (2 nights = $240)"
            status = f"Occupied by {guest['name']} ({guest['nights']} nights = ${guest['cost']})"
        print(f"ROOM {room} | {ROOMS[room]['type']} |  ${ROOMS[room]['rate']}/night | {status}")
    print(f"Total earned: ${hotel['total_earned']}")

while is_on:
    user_choice = input("What would you like? (book/checkout/report/quit): ")
    if user_choice == "quit":
        is_on = False
    elif user_choice == "report":
        report(ROOMS)
    elif user_choice == "book":
        room_type = input("What room type would you like? (single/double/suite):")
        print(book(room_type))
    elif user_choice == "checkout":
        checkout_room = input("Enter the room number to checkout: ")
        print(checkout(checkout_room))
    else:
        print("Invalid choice")

