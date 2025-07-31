#!/bin/bash

# Build and run the Docker container
echo "Building and starting CrewAI Crash Course Docker container..."
docker-compose up --build -d

# Print instructions
echo ""
echo "CrewAI Crash Course is now running!"
echo ""
echo "Access Jupyter Notebook in your browser:"
echo "http://localhost:8888"
echo ""
echo "To run specific examples, connect to the container:"
echo "docker exec -it crewai-crash-course-crewai-1 bash"
echo "Then run: python run.py"
echo ""
echo "To stop the container:"
echo "docker-compose down"