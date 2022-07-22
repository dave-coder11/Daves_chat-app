from vidstream import AudioSender
from vidstream import AudioReceiver
import threading
import keyboard


receiver = AudioReceiver('192.168.219.30', 9999)
receive_thread = threading.Thread(target=receiver.start_server)
try:
    receive_thread.start()
except:
    print("the client disconected")