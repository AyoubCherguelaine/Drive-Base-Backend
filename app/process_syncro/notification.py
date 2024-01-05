from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit


class notification_system:

    def __init__(self, app:Flask) -> None:
        
        self.socketio =SocketIO(app, cors_allowed_origins="*")
        self.app = app
        
        #events 
        self.socketio.on('connect')(self.connect)
        self.socketio.on('disconnect')(self.disconnect)
        self.socketio.on('create_room')(self.create_room)
        self.socketio.on('finish_process')(self.finish_process)
        
    def connect(self):
        pass
        
    def disconnect(self):
        pass
        
    def create_room(self, data):
        room = data['room']
        join_room(room)
        
    def finish_process(self, data):
        room = data['room']
        job_id = data['job_id']
        emit('broadcast_finish_process', {'job_id': job_id}, room=room)

    
    def run(self):
        self.socketio.run(self.app, debug=True)
