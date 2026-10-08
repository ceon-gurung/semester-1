# Week 1.2, Session 2: Task 6

import datetime

machine_temperature = int(input("Enter the machine's temperature in degrees Celsius: "))
machine_pressure = int(input("Enter the machine's pressure in PSI: "))
machine_operational_status = int(input("Enter machine's operational status (1 for operating, 0 for stopped): "))

if machine_operational_status == 0:
  print("The machine is stopped and no immediate action is needed.")
elif machine_operational_status == 1:
    if machine_pressure > 100:
        print("High pressure is detected. Maintenance is recommended.")
    elif 70 <= machine_pressure <= 100:
         print("The pressure is stable.")
    else:
         print("The pressure is low and the system is operating normally.")

    if machine_temperature > 80:
        print("The temperature is too high. It is recommended to shut down the machine.")
    elif 50 <= machine_temperature <= 80:
        print("The temperature is within safe limits.")
    else:
        print("The machine temperature is low and no action is needed.")
else:
  print("invalid machine operational status detected")

f = open("week1.2/session2/task6/machine_log.txt", 'a')
f.write(f"Time:                                                              {datetime.datetime.now()}\n")
f.write(f"Machine temperature (Celsius):                                     {machine_temperature}\n")
f.write(f"Machine pressure (PSI):                                            {machine_pressure}\n")
f.write(f"Machine's operational status (1 for operating, 0 for stopped):     {machine_operational_status}\n")
f.write("\n")

f.close()