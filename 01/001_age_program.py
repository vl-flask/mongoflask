def age_program():
    seconds_or_years = input("Give me seconds (s) or years (y)? ")
    if seconds_or_years == 's':
        # Convert seconds to years
        user_value = input("Enter the number of seconds you've lived for: ")
        years = user_value/(60*60*24*365)
        print(f"You've lived for {years} years.")
    elif seconds_or_years == 'y':
        user_value = input("Enter the number of years you've lived for: ")
        seconds = int(user_value) * 60*60*24*365
        print(f"You've lived for {seconds} seconds.")

age_program()
