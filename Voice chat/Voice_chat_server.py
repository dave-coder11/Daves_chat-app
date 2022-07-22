from vidstream import AudioSender
import threading

sender = AudioSender('192.168.219.30', 9999)
sender_thread = threading.Thread(target=sender.start_stream)

sender_thread.start()