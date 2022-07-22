from vidstream import AudioReceiver
import threading

receiver = AudioReceiver('192.168.219.30', 9999)
receive_thread = threading.Thread(target=receiver.start_server)

receive_thread.start()