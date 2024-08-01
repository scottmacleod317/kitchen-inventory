FROM python:3.12.4-slim


ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

ENV PORT=1234

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

CMD exec uvicorn src.main:app --host 0.0.0.0 --port ${PORT} --workers 1
