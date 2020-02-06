FROM python:3
WORKDIR /app
COPY ./app /app
RUN pip3 install --trusted-host pypi.python.org Flask
RUN pip3 install sklearn
RUN pip3 install pandas
RUN pip3 install numpy
CMD ["python3", "app.py"]

# docker build -t titanic_app .
# docker run --rm -p 9001:9000 titanic_app