import time;

# timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
timestamp = time.strftime("%H:%M:%S");
hr = int(time.strftime("%H"));
min = int(time.strftime("%M"));
sec = int(time.strftime("%S"));
print(timestamp);

if(hr < 12): 
    print("Good Morning");
elif(hr < 16): 
    print("Good Afternoon");
else: 
    print("Good Evening");