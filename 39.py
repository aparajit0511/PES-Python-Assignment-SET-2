import calendar  
    
yy = 2020
mm = 5
 
print(calendar.month(yy, mm))  

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string) 
