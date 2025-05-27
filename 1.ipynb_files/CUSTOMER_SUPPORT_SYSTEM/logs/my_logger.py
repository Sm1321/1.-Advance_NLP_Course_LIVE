import logging
import os
from datetime import datatime





LOG_FILE = f"{datatime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)


os.makedirs(logs_path,exist_ok = True)


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logger = logging.getLogger("my_agentic_app")

logging.basicConfig(
    
    filename = LOG_FILE_PATH,
    
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
    level = logging.INFO,
)

logger.info("this is my testing message")