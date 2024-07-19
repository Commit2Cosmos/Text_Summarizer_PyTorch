FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        && rm -rf /var/lib/apt/lists/*


COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv && pipenv install --dev --deploy


CMD ["sh", "-c", "pipenv run python app.py"]