import os
import re
from typing import final
print("Shut Down Time V1.0")
time = input("Give Value To Timer To Shutdown:")

num = re.sub(r"[a-zA-Z ]", "", time) 
unit = re.sub(r"[0-9]", "", time) 

print(num)
print(unit)



#For Seconds
if unit == "sec":
    final = int(num) * 1

#For Minutes
if unit == "mins" or " mins":
    final = int(num) * 60

#For Hours
if unit == "hour":
    final = int(num) * 3600
#For Days
if unit == "days":
    final = int(num) * 3600 * 24



print(final) 