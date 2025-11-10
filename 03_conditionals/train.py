seat_type=input("Enter seat type (sleeper/ac/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("No ac ,beds available")
    case "ac":
        print("bed with ac ")
    case "general":
        print("bas kursi milegi")
    case "luxury":
        print("Bade log ")
    case _:
        print("Invalid seat type")
