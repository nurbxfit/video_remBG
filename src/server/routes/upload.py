from flask_restful import Resource, Api
from flask import request
from threading import Thread

import os 
from utils.cleaner import clear_folder
from utils.process import process_video

UPLOAD_FOLDER= os.path.join('uploads')
EXTRACTED_FRAMES_FOLDER = 'output/extracted'
BACKGROUND_REMOVED_FOLDER = 'output/cleaned'
FINAL_VIDEO_OUTPUT = os.path.join('output/final')
FRAME_RATE = 24

class Upload(Resource):
    def get(self):
        return {'Hello': 'world'}
    
    def post(self):
        # return {request}
        if 'file' not in request.files:
            return {'message': 'No file provided'}, 400
        
        file = request.files['file']

        if file.filename == '':
            return {'message': 'No selected file'}, 400
        
        clear_folder(UPLOAD_FOLDER)
        SOURCE_FILE = f'{UPLOAD_FOLDER}/{file.filename}'
        file.save(SOURCE_FILE)
        # run some processing function (not blocking the return response)
        # Start processing in a separate thread
        bg_remove_thread = Thread(target=process_video, kwargs={
            'SOURCE_FILE': SOURCE_FILE,
            'EXTRACTED_FRAMES_FOLDER': EXTRACTED_FRAMES_FOLDER,
            'BACKGROUND_REMOVED_FOLDER': BACKGROUND_REMOVED_FOLDER,
            'FINAL_OUTPUT_VIDEO': FINAL_VIDEO_OUTPUT,
            'FRAME_RATE': FRAME_RATE
        })
        bg_remove_thread.start()

        return {'message': 'File uploaded successfully', 'filename': file.filename}
    
    def cleanup(self):
        # Perform cleanup tasks after processing is complete
        # For example, deleting temporary files or logging
        pass
