def life_in_weeks(age):
    whole_weeks = 90 * 52.1429
    print(f"You have {(whole_weeks - (int(age) * 52.1429)):.0f} weeks left.")


current_age = input("What is your age? ")

life_in_weeks(current_age)
