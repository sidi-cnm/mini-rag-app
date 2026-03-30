from .baseController import baseController
import os


class ProjectController(baseController):

    
    def __init__(self):
        super().__init__()


    def get_project_path(self, project_id: str):
        project_path = os.path.join(self.projects_path, project_id)

        if not os.path.exists(project_path):
            os.makedirs(project_path)
        return project_path    
    

    