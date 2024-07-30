import subprocess
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Now you can access the environment variables
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
BACKUP_FILE="mysql_backup_$(date +'%Y-%m-%d_%H-%M-%S').sql"
#BACKUP_FILE = f"mysql_backup_{now.strftime('%Y-%m-%d_%H-%M-%S')}.sql"
print(BACKUP_FILE)

cmd = f"mysqldump -h {DB_HOST} -u {DB_USER} -p{DB_PASSWORD} {DB_NAME} > {BACKUP_FILE}"
subprocess.run(cmd, shell=True)
