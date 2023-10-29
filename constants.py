import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

file_path = os.getenv('FILE_PATH')
