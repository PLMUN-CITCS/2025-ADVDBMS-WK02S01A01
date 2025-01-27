FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=your_strong_password 
ENV MYSQL_DATABASE=your_database_name

# Copy your example SQL scripts (if any)
COPY ../scripts/create_tables.sql /docker-entrypoint-initdb.d/ 
COPY ../scripts/insert_data.sql /docker-entrypoint-initdb.d/ 

# Expose the MySQL port
EXPOSE 3306