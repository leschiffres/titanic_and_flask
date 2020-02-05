FROM python:3
WORKDIR /app
ADD ./app /app
RUN pip3 install --trusted-host pypi.python.org Flask
RUN pip3 install sklearn
CMD ["python", "app.py"]

# docker run --rm -p 5002:50001 titanic_app
