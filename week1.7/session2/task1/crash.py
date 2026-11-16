# Week 1.7, Session 2: Task 1 - IndexError

# Run this program and observe what happens

def assign_values(x):
    for i in range(100):
        x[i] = (i + 1) * (i + 1);

if __name__ == "__main__":
    data = [0] * 100                # data was set to [0] * 10, but assign_values(x) set values for 100 indexes of data
    assign_values(data)
    print("Done!")