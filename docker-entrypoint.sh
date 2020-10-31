#!/bin/bash

# Apply database migrations
echo "Apply database migrations..."
python manage.py migrate

# Load csv to postgres database
echo "Populating data base..."
python manage.py get_data

# Load lat lon from Google maps API
echo "Load latitude and longitude from Google maps API"
python manage.py get_lat_lon

# Start server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000
