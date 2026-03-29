from .baseController import baseController
from fastapi import UploadFile, File

class DataController(baseController):

    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Convert bytes to MB

    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in  self.app_settings.File_Allowwed_types:
            return False,"File type not allowed."
        
        if file.size > self.app_settings.File_max_size * self.size_scale:
            return False,"File size exceeds the maximum limit."
        

        return True,"File is valid."   