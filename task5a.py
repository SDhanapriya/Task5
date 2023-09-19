my_age = int(input("Enter my age: "))
your_age =int(input("Enter your age: "))

if my_age > your_age and my_age - your_age !=1:
    print("I am", your_age - my_age,"years older than you.")
    if my_age - your_age == 1:
        print("I am a year older than you.")