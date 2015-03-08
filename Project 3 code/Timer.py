import Tkinter as tk
#at the moment i have made a sorta stop watch 
def update_timeText():
  if (state):
    global timer
    #here is where you change the value of what it counts up/down in
    timer[2] -=1
    if (timer[2] >= 60):
        timer[2] = 0
        timer[1] += 1
    if (timer[1] >= 60):
        timer[0] += 1
        timer[1] = 0
    timeString = pattern.format(timer[0], timer[1], timer[2])
    return timeString

# Step 1        
global state      
global timer    
state = True
timer = [0, 0, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'

# Step 2
#every time this is called it prints the next number in the count down/up in
#the side window 
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()
print update_timeText()



