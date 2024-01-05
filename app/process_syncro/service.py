from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
import threading

class service:
    
    def __init__(self, app :Flask):
        self.app= app
        
    def process(self):
        data = request.json
        return "finish"
    
    def async_process(self):
        data = request.json
        return "finish"
    
    def get_status(self,job_id):
        pass
    
    def __finish_process(self):
        pass
    
    def __generate_job_id(self):
        return 'job_id'
    
    def __create_room(self,job_id):
        pass