from .baseController import baseController
from .ProjectController import ProjectController
from models import ResponseStatus
from fastapi import UploadFile, File
import os

class DataController(baseController):

    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Convert bytes to MB

    def validate_uploaded_file(self, file: UploadFile):
       
        if file.content_type not in  self.app_settings.File_Allowwed_types:
            return False,ResponseStatus.File_Not_allowed.value
        
        if file.size > self.app_settings.File_max_size * self.size_scale:
            return False,ResponseStatus.File_size_exceed.value
        

        return True,ResponseStatus.File_is_Valid.value  
    

    def generate_unique_filename(self, original_filename: str, project_id: str):
        
        random_key = self.random_string_generator()
        
        file_name_cleaned = self.clean_name_file(original_filename)

        path_project = ProjectController().get_project_path(project_id = project_id)

        new_filename = f"{random_key}_{file_name_cleaned}"
        new_file_project = os.path.join(path_project, new_filename)
        
        while os.path.exists(new_file_project):
            random_key = self.random_string_generator()
            new_filename = f"{random_key}_{file_name_cleaned}"
            new_file_project = os.path.join(path_project, new_filename)
        
        return new_file_project , new_filename

        return new_file_project
    
    def clean_name_file(self, filename: str):
        filename = filename.replace(" ", "_")
        filename = "".join(c for c in filename if c.isalnum() or c in ['_', '.'])
        return filename