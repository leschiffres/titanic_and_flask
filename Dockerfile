FROM python:3
WORKDIR /app
COPY ./app /app
RUN pip3 install --trusted-host pypi.python.org Flask
RUN pip3 install sklearn
CMD ["python3", "app.py"]

# docker run --rm -p 5002:50001 titanic_app