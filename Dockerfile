FROM python:3.9-slim-buster
ARG APP
WORKDIR /app
COPY ./apps/$APP .
RUN pip3 install -r requirements.txt
CMD ["python3","main.py"]