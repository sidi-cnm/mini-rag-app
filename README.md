# mini-rag-app

## Description
   This is a simple RAG (Retrieval-Augmented Generation) application that allows users to ask questions and get answers based on a provided context. The application uses a pre-trained language model to generate responses and a vector store to retrieve relevant information from a given context.


## Requirements 
## first thing install python 3.8 or late



## Installation conda and creation of the env viretuelle 
1) Install conda form the web site officiel of conada
2) create a new envirment with the following command
   ```bash
   $conda create -n envirment_name python=3.8
   ```
 3) activate the envirment with the following command  
    ```bash
    $conda activate envirment_name
    ```
4) install the requirements with the following command
   ```bash
   $pip install -r requirements.txt
   ```

## setup the env viruable 
 ```bash
 cp .env.example .env
 ```

 
## Run the application
```bash
uvicorn main:app --reload
