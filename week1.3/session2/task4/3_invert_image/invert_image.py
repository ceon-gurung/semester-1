# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

# Create inverted image
# the formula: invert_pixel_value = max_gray - original_pixel_value


# write the inverted pgm image to a new file.
# Remember to include:
# - the string `P2`
# - the width and height dimensions
# - maximum gray value
# - you could convert numbers in a list to strings and join them with spaces
#   for example line = [255, 255, 0, 255, 255]
#   string_line = " ".join(str(item) for item in line)
#   # output: string_line = "255 255 0 255 255"

try:
    with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm", 'w') as f:
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