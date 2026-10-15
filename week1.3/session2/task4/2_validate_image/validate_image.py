# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

try:
    with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm", 'r') as f:
        contents = f.readlines()
        raw_dimensions = contents[1]
        height = width = 0
        dimension = ""
        for char in raw_dimensions:
            dimension += char
            if char == ' ':
                width = int(dimension) # First dimension finish
                dimension = ""
        height = int(dimension) # Second dimension finish

        max_gray_value = contents[2]
except:
    print("Error, file not found at location: /workspaces/semester-1/week1.3/session2/task4/images/feep.pgm")

print(width)
print(height)
print(max_gray_value)

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
gray_invalid_flag = False
try:
    with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm", 'r') as f:
        contents = f.readlines()
        count_row = 0
        for i in range(len(contents)):
            if (i > 2): # if not the metadata lines

                # construct and validate a pixel
                count_row += 1 # another row
                pixel_gray_value = ""
                count_column = 0 # this is to count the number of pixels on a row
                for j in range(len(contents[i])): # go through each line
                    if (contents[i][j] == ' ') and (pixel_gray_value != ""): # if end of a pixel AND pixel isn't empty
                        count_column += 1 # another column
                        if 0 <= int(pixel_gray_value) <= 15: # if between 0-15
                            #print(f"Valid pixel_gray_value at line {i} column {j}")
                            pass
                        else:
                            #print(f"Invalid pixel_gray_value at line {i} column {j}")
                            gray_invalid_flag = True
                        pixel_gray_value = "" # clear out checked pixel
                    else: # if the character is not a space
                        pixel_gray_value += contents[i][j] # add a character

                # do the pixel validation again because the for loop doesn't expect a space at the end of a row
                count_column += 1
                if 0 <= int(pixel_gray_value) <= 15: # if between 0-15
                    #print(f"Valid pixel_gray_value at line {i} column {j}")
                    pass
                else:
                    #print(f"Invalid pixel_gray_value at line {i} column {j}")
                    gray_invalid_flag = True
                pixel_gray_value = "" # clear out checked pixel
except:
    print("Error, file not found at location: /workspaces/semester-1/week1.3/session2/task4/images/feep.pgm")

print(count_column)
print(count_row)





# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value

if (width != count_column):
    print("Invalid width")
elif (height != count_row):
    print("Invalid height")
elif gray_invalid_flag:
    print("Invalid pixel values")
else:
    print("Valid image")