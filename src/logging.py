import logging
from datetime import datetime
import os


Log_file= {datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log
file_path= os.path.join(os.getcwd(), "LOGS")
os.makedirs(file_path, exist_ok=True)
Log_file_path = os.path.join(file_path, Log_file)


logging.basicConfig(
    filename=Log_file_path,
    format="[%(asctime)s] %(lineno)d % (levelname)s %(message)s" ,
    level=logging.info
)
