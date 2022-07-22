from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import keyboard

while True:
    sender = AudioSender('192.168.219.30', 9999)
    sender_thread = threading.Thread(target=sender.start_stream)
    try:
        sender_thread.start()
    except:
        print("the client disconected")