
from controller.baseController import baseController
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyMuPDFLoader  # ✅ Works

from langchain_text_splitters import RecursiveCharacterTextSplitter

from controller.ProjectController import ProjectController
import os
from models import ProcessStatus

class ProcessController(baseController):
    

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.projects_path = ProjectController().get_project_path(project_id = project_id)
        super().__init__()




    def get_file_extension(self, file_id: str):
        return file_id.split(".")[-1]
    
    def get_file_loader(self, file_id: str):

        extension = self.get_file_extension(file_id)
        
        file_path = os.path.join(self.projects_path, self.project_id, file_id)


        if extension == ProcessStatus.TXT.value:
            return TextLoader(file_path, encoding="utf-8")
        
        elif extension == ProcessStatus.PDF.value:
            return PyMuPDFLoader(file_path)
       
        return None
    

    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(file_id)
        return loader.load()
    
    def process_file_content(self, file_id: str, file_content : list ,chunk_size:int=100, chunk_overlap :int =20):
        # content = self.get_file_content(file_id)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
            )
        
        # file_Content = [
        #     rec.page_content for rec in file_content
        # ]

        # meta_data_content = [
        #     rec.metadata for rec in file_content
        # ]

        chunks = text_splitter.split_documents(
            file_content
            )
        return chunks