import os
import re
from typing import final
print("Shut Down Time V1.0")
int_time = input("Give Value To Timer To Shutdown:")
time = int_time.replace(" ", "")

num = re.sub(r"[a-zA-Z ]", "", time) 
unit = re.sub(r"[0-9]", "", time) 


#For Seconds
if unit == "sec":
    final = int(num) * 1

#For Minutes
elif unit == "mins":
    final = int(num) * 60

else:
    print("Enter Valid Unit")


os.system('cmd /k shutdown /s /t '+ str(final))

