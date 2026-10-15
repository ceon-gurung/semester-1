# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

try:
    with open("/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm", 'r') as f:
        contents = f.readlines()
        raw_dimensions = contents[1]
        dimensions = [0, 0]
        dimension = ""
        for char in raw_dimensions:
            dimension += char
            if char == ' ':
                dimensions[0] = dimension # First dimension finish
                dimension = ""
        dimensions[1] = dimension # Second dimension finish

        max_gray_value = contents[2]
except:
    print("Error, file not found at location: /workspaces/semester-1/week1.3/session2/task4/images/feep.pgm")

for value in dimensions:
    print(value)

print(max_gray_value)

# Read the file content

# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)