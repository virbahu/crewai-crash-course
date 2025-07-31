FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY config/ ./config/
COPY marketing-crew/ ./marketing-crew/
COPY *.ipynb .
COPY *.py .

RUN pip install --no-cache-dir crewai crewai-tools google-generativeai python-dotenv jupyter

EXPOSE 8888

CMD ["bash"]