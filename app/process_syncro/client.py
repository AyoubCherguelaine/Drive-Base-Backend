import socketio
import time

class client:
    def __init__(self, server_url) -> None:
        self.server_url = server_url
        self.socket = socketio.Client()
        self.connected= False
        
        self.socket.on('connect')(self.on_connect)
        self.socket.on('disconnect')(self.on_disconnect)
        self.socket.on('broadcast_finish_process')(self.finish_process)
        
        
    
    def on_connect(self):
        self.connected = True
    
    def on_disconnect(self):
        self.connected = False
    
    def start_Processing_(self):
        pass
    
    def start_async_process(self):
        pass
    
    def get_result(self, job_id):
        pass
    
    def finish_process(self, data):
        pass
    
    def check_status(self,job_id):
        pass
    
    def run(self):
        self.socket.connect(self.server_url)
        
    
    