from app import db
from app.base.endpoint import endpoint
from ..models.buckets import bucket as bucket_model

from flask import Flask, request, send_file
import os

class Bucket(endpoint):
    
    def __init__(self):
        super().__init__(bucket_model,'bucket')
        
        