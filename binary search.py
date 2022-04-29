#Binary search algoithm
#The user choose a number beetween 1 and 100 and the programm have to guess it

def binary_search():

    start_index = 0
    end_index = 100
    mid_index = 50

    times = 1

    user_choice = str(input("Is it your number: " + str(int(mid_index)) + ", or is it higher or lower? y/h/l: "))

    while user_choice != "y":
        times += 1
        
        if user_choice == "h":
            start_index = mid_index+1
        elif user_choice == "l":
            end_index = mid_index-1
        mid_index = (start_index+end_index)/2
        
        user_choice = str(input("Is it your number: " + str(int(mid_index)) + ", or is it higher or lower? y/h/l: "))
        
    print("Oh, that was harder... but it took only " + str(times) + " times to guess your number!")
    
print("Hello! Welcome in my world!")
print("Choose a number between 1 and 100 and I'll try to guess it!")
print("Wish me luck :)")

binary_search()
