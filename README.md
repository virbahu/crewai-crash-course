# CrewAI Crash Course

Crash course tutorial for CrewAI framework

## Overview

This repository contains examples and tutorials for the CrewAI framework, which allows you to create AI agent systems. The examples range from simple email agents to complex marketing crews.

## Requirements

To run the examples directly, you need:
- Python 3.10 or higher
- Required Python packages: `crewai`, `crewai-tools`, `google-generativeai`, `python-dotenv`

## Docker Setup (Recommended)

The easiest way to run this project is using Docker:

1. Make sure you have [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

2. Run the Docker container:
   - On Windows: Double-click `run-docker.bat` or run it from the command line
   - On macOS/Linux: Run `./run-docker.sh` (you might need to make it executable with `chmod +x run-docker.sh`)

3. Access Jupyter Notebook in your browser at: http://localhost:8888

4. To run specific examples, connect to the container:
   ```bash
   docker exec -it crewai-crash-course-crewai-1 bash
   python run.py
   ```

## Running Examples Without Docker

If you prefer not to use Docker, you can run the examples directly:

1. Install the required packages:
   ```bash
   pip install crewai crewai-tools google-generativeai python-dotenv jupyter
   ```

2. Run the examples:
   - Jupyter Notebooks: `jupyter notebook`
   - Python scripts: `python 5_yaml.py`, `python 6_memory.py`, etc.
   - Marketing crew: `cd marketing-crew && python crew.py`

## Examples

1. `1_email_agent.ipynb` - Basic email agent example
2. `2_email_agent_with_tool.ipynb` - Email agent with tools
3. `3_crew.ipynb` - Basic crew example
4. `4_crew_with_tools.ipynb` - Crew with tools
5. `5_yaml.py` - YAML configuration example
6. `6_memory.py` - Memory example
7. `marketing-crew/crew.py` - Complete marketing crew implementation

## References

- Google reference article: https://ai.google.dev/gemini-api/docs/crewai-example
- CrewAI documentation: https://docs.crewai.com