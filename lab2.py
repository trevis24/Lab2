print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    number=input("Enter numbers: ")
    number_list=number.split(",")
    float_list=[]
    for num in number_list:
        float_list.append(float(num))

    return float_list

def calc_average(temperatures):
    average=sum(temperatures)/len(temperatures)
    return average

def find_min_max(temperatures):
    min_temp=min(temperatures)
    max_temp=max(temperatures)
    return[min_temp,max_temp]

def sort_temperature(temperatures):
    print("sort_temperature")

def calc_median_temperature(temperatures):
    print("calc_median_temperature")
