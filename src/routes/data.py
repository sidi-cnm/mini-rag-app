from fastapi import FastAPI ,APIRouter ,Depends , File , UploadFile , status
from fastapi.responses import JSONResponse  
from helpers.config import get_settings ,Settings
from controller import DataController, ProjectController
import aiofiles
import os
from models import ResponseStatus
import logging

logger = logging.getLogger("uvicorn.error")


data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id:str , file :UploadFile , app_settings : Settings = Depends(get_settings)):

    DataController_obj = DataController()
    is_valid , message_type = DataController_obj.validate_uploaded_file(file = file)



    if not is_valid:
        return JSONResponse(content={"message": message_type}, status_code=status.HTTP_400_BAD_REQUEST)
    
    file_path = ProjectController().get_project_path(project_id = project_id)

    file_path, file_id =DataController_obj.generate_unique_filename(original_filename=file.filename, project_id=project_id)
         
    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
         while chunk := await file.read(app_settings.File_chunk_size):
                await out_file.write(chunk)


    except Exception as e:
        logger.error(f"Error while uploading file: {e}")
        return JSONResponse(content={"message": ResponseStatus.File_Upload_Failed.value}, status_code=status.HTTP_400_BAD_REQUEST)
        


    return JSONResponse(content={
        "message": ResponseStatus.File_is_Uploaded.value ,
        "file_id": file_id
        }, )


