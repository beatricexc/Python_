from datetime import datetime

even =[0,2, 4, 6, 8, 10, 12, 14, 16,18, 20, 22, 24, 26, 28 ,30,32, 34, 36, 38,40,42,46,48,50,52.54,56.58,60]

time_right_now= datetime.today().minute

if time_right_now in even:
    print("I'd say we're even")
else:
    print("We're not even yet!")
