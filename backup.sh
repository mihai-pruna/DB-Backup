#!/bin/bash

# Set the database credentials and backup file name
DB_HOST="localhost"
DB_USER="your_username"
DB_PASSWORD="your_password"
DB_NAME="your_database"
BACKUP_FILE="mysql_backup_$(date +\%Y-\%m-\%d).sql"

# Dump the database to a SQL file
mysqldump -h $DB_HOST -u $DB_USER -p$DB_PASSWORD $DB_NAME > $BACKUP_FILE

# Print a success message
echo "MySQL database backup complete: $BACKUP_FILE"
