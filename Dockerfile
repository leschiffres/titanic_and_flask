FROM python:3
WORKDIR /app
COPY ./app /app
RUN pip3 install --trusted-host pypi.python.org Flask
RUN pip3 install sklearn
CMD ["python3", "app.py"]

# docker build -t titanic_app .
# docker run --rm -p 5001:5001 titanic_app