FROM python:3.12-slim

ENV APP_FOLDER=/app

WORKDIR $APP_FOLDER

COPY . $APP_FOLDER

RUN pip install -r requirements.txt

VOLUME ["./names"]

ENTRYPOINT ["python", "main.py"]

# docker run -v ./names:/app/names -it 35feb5f