import keyboard
import time
import datetime

currentTime = datetime.datetime.now() # current time
hoursLeft = 25-currentTime.hour # hrs until 1:?? AM

print("I'll run the command in ", hoursLeft, " hours.")
time.sleep(60*60*hoursLeft) # wait until the right time

currentTime = datetime.datetime.now() # update time for the console
print("[autoRejoin]: rejoining the server at %s:%s" % (currentTime.hour, currentTime.minute))

# turn this into a for loop later
keyboard.press_and_release('t') # opens the chat and types out the command.
time.sleep(.5)
keyboard.write('/')
time.sleep(.1)
keyboard.write('g')
time.sleep(.1)
keyboard.write('o')
time.sleep(.1)
keyboard.write(' ')
time.sleep(.1)
keyboard.write('o')
time.sleep(.1)
keyboard.write('p')
time.sleep(.2)
keyboard.write('s')
time.sleep(.3)
keyboard.write('k')
time.sleep(.1)
keyboard.write('y')
time.sleep(.2)
keyboard.write('b')
time.sleep(.2)
keyboard.write('l')
time.sleep(.1)
keyboard.write('o')
time.sleep(.3)
keyboard.write('c')
time.sleep(.2)
keyboard.write('k')
time.sleep(.3)
keyboard.press_and_release('enter')
time.sleep(9)
keyboard.press_and_release('esc')
print("The deed is done. bye.")
exit()
