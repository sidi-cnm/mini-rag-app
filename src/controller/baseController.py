from helpers.config import get_settings ,Settings
import os
import random
import string


class baseController:

    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.projects_path = os.path.join(self.base_dir, '../assets/files')


    def random_string_generator(self, length=12):
        
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))    