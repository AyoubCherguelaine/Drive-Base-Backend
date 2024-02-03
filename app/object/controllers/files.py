from app import db
from app.base.endpoint import endpoint
from ..models.file import file as file_model

from flask import Flask, request, send_file
import os



from app.users.models.users import User

class File(endpoint):
    def __init__(self ):
        super().__init__(file_model, 'file', True)

    def upload_file():
        user = User.get_user_from_token()
        if 'file' not in request.files:
            return 'No file part'

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return 'No selected file'
        
        state = file_model.upload_file(uploaded_file,user)
        return 'File uploaded successfully'
    
    def download_file(filename):
        # Specify the path where your files are stored
        file_path = os.path.join('uploads', filename)

        # Check if the file exists
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return 'File not found'