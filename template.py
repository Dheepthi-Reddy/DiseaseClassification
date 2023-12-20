import os
from pathlib import Path
import logging

# log format to be dispalyed, INFO: is the information level of the log, asctime: time at whoch the log is generated
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

# Specifying the project name
project_name = "cnnClassifier"

# list of files or folder want to be created
list_of_files = [

    #github folder, inside that workflows, inside that gitkeep folder
    ".github/workflows/.gitkeep", 

    # source folder with f string, since its a local package we need to specify the constructor
    f"src/{project_name}/__init__.py ",

    # creating a components folder and specifying the constructor
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init_.py",
    f"src/{project_name}/entity/__init_.py",
    f"src/{project_name}/constants/__init_.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "template/index.html" # to create templates

]


for filepath in list_of_files:

    # defining the path type, because we used forward slashing where as windws uses backslash
    filepath = Path(filepath)

    # it will seperate the file path and file name
    filedir, filename = os.path.split(filepath)

    # creating directory
    # file directory is not empty
    if filedir != "":

        # exist_ok is used when the directory already exists it won't create again
        os.makedirs(filedir, exist_ok = True)

        # logging information with the file directory and file name
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # checking if the path exists or not, checking the size of the file
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):

        # w: rite mode
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:

        # if the file aleady exists
        logging.info(f"(filename) already exists")