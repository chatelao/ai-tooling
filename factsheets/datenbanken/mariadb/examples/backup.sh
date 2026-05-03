#!/bin/bash
# Backup script example
DB_NAME="myapp"
BACKUP_PATH="/backups/$(date +%Y%m%d)_${DB_NAME}.sql"
mysqldump -u root -p ${DB_NAME} > ${BACKUP_PATH}
echo "Backup saved to ${BACKUP_PATH}"
