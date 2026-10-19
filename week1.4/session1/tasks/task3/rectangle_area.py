
# function implementation

def rectangle_area(height, width):  # define suitable input data
    # ...               # implement the function
    return height * width              # return an appropriate value

# testing the function

print(f"Area is {rectangle_area(5, 20)}")   # provide suitable data matching your inputs


# accept an integer value and returns a list of even integers between 0 and that value.​

max = int(input("Enter a number "))

for i in range(max):
    if (i%2 == 0):
        print(i)

# accept a list of integers and returns the mean average of the list.​

ints = input("Enter a list of numbers, separated by a single space")
intList = [int(i) for i in ints.split(" ")]

print("Mean average of your list: " + str(sum(intList)/len(intList)))