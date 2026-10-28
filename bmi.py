def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi= weight/(height*height)
    print(f"Your BMI is {bmi:.2f}")

    if bmi<18.5:
        print("You are Under Weight")
    elif bmi>=18.5 or bmi<=25:
        print("You are Normal")
    elif bmi>25:
        print("You are Over Weight")



calculate_bmi(weight=57, height=1.73)