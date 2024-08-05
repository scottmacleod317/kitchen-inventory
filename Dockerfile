FROM python:3.12.4-slim

ARG INSTANCE_CONNECTION_NAME
ARG DB_USER
ARG DB_PASS
ARG DB_NAME

ENV INSTANCE_CONNECTION_NAME=$INSTANCE_CONNECTION_NAME
ENV DB_USER=$DB_USER
ENV DB_PASS=$DB_PASS
ENV DB_NAME=$DB_NAME

ENV APP_HOME=/app
WORKDIR $APP_HOME
COPY . ./

ENV PORT=1234

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

CMD exec uvicorn src.main:app --host 0.0.0.0 --port ${PORT} --workers 1
