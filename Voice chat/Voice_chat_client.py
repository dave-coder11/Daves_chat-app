from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import keyboard

while True:
    try:
        if keyboard.is_pressed('t'):  # if key t is pressed 
            receiver = AudioReceiver('192.168.219.30', 9999)
            receive_thread = threading.Thread(target=receiver.start_server)
        else:
            sender = AudioSender('192.168.219.30', 9999)
            sender_thread = threading.Thread(target=sender.start_stream)
    except:
        print('something whent wrong pleas try later')
        break
            
    try:
        sender_thread.start()
    except:
        print("the client disconected")
        break