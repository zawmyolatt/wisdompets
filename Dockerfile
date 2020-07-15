# base image
FROM alpine:3.7

# Install python 3 and pip
RUN apk add --update python3

# Install Python modules needed by the Python app
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

# Tell the port number the container should expose
EXPOSE 5000

# Run the application
CMD ["python3", "/usr/src/app/manage.py", "startserver"]