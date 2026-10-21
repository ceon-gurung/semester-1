filename = input("")
# open the file
with open(filename, 'r') as f:
    contents = f.readlines()
    contents.pop(0)
    gradeEntries = []
    for i in contents:
        temp = i.split(',')
        gradeEntry = temp[0] + ","
        temp.pop(0)

        total = 0
        count = 0
        mean = 0
        grade = ""
        for num in temp:
            try:
                total += int(num)
                count += 1
            except:
                pass

        mean = total/count
        if (mean >= 70):
            grade = "1"
        elif (mean >= 60):
            grade = "2:1"
        elif (mean >= 50):
            grade = "2:2"
        elif (mean >= 40):
            grade = "3"
        else:
            grade = "F"

        gradeEntry += f"{total/count:.2f}" + "," + grade + "\n"
        gradeEntries.append(gradeEntry)

    new_filename = input() + "_out.csv"
    with open(new_filename, 'a') as g:
        g.writelines(gradeEntries)