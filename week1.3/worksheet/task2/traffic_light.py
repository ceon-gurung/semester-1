states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())

state = "red"

for i in range(maxtime):
    if not (systime > maxtime):
        if state == "red":
            for j in range(4):
                print(f"Time {systime:03} State {state}")
                systime += 1
                if systime > maxtime:
                    break
            state = "red_amber"

        elif state == "red_amber":
            for j in range(3):
                print(f"Time {systime:03} State {state}")
                systime += 1
                if systime > maxtime:
                    break
            state = "green"
        
        elif state == "green":
            for j in range(5):
                print(f"Time {systime:03} State {state}")
                systime += 1
                if systime > maxtime:
                    break
            state = "amber"
        
        elif state == "amber":
            for j in range(3):
                print(f"Time {systime:03} State {state}")
                systime += 1
                if systime > maxtime:
                    break
            state = "red"

        else: pass