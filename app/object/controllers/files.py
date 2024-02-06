from app import db
from app.base.endpoint import endpoint
from ..models.file import file as file_model

from flask import Flask, abort, jsonify, request, send_file
import os



from app.users.models.users import User

class File(endpoint):
    def __init__(self ):
        super().__init__(file_model, 'file', True)

    def upload_file(self):
        user = User.get_user_from_token()
        if not user:
            abort(403,"User Problem") 
        if 'file' not in request.files:
            abort(500,"there is no File ~~") 

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            abort(500,"File name ~~") 
        
        try:
            new_file = file_model.upload_file(uploaded_file, user)
            return jsonify(new_file.json_populate())
        except Exception as e:
            # Handle exceptions appropriately
            abort(500,f"File name e: {str(e)}")
    
    def download_file(filename):
        # Specify the path where your files are stored
        file_path = os.path.join('uploads', filename)

        # Check if the file exists
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return 'File not found'