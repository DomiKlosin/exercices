#Binary search algoithm version 2.0
#The user choose a number beetween 1 and 100 and the programm have to guess it

#I had a problem with IndexError and I aksed this question on StackOverFlow (first time)
#This resolution is from user @trincot - thank you :)

def binary_search():
    numbers = list(range(100))

    start_index = 0
    end_index = len(numbers) - 1

    times = 0
    while True:  # avoid code repetition, and break in middle of loop
        mid_index = (end_index+start_index)//2
    
        user_choice = int(input("Is this your number: " + str(numbers[mid_index]) + "?\n"
             + "0 - your number is lower,\n"
             + "1 - it's your number,\n"
             + "2 - your number is higher: "))
        times += 1
        if user_choice == 1:
            break
        if user_choice == 0 and mid_index > start_index:
            end_index = mid_index-1
        elif user_choice == 2 and mid_index < end_index:
            start_index = mid_index+1
        else:
            print("Invalid input")

    print("Oh, that was hard... but it took only " + str(times) 
        + " times to guess your number!")

print("Hello! Welcome in my world!")
print("Choose a number between 1 and 100 and I'll try to guess it!")
print("Wish me luck :)")

binary_search()
