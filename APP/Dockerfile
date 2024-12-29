FROM base-image:latest
WORKDIR /model_app
COPY . /model_app
# Set the FLASK_APP environment variable if flask app is inside a file with different name than app.py
# so flask can find the app
ENV FLASK_APP=spam_detection.py 
EXPOSE $APP_DOCKER_PORT
CMD ["flask", "run","--host=0.0.0.0"] 
# The --host=0.0.0.0 option makes Flask listen on any other network the container is connected to. 
# This is necessary for Docker to map the port correctly from the container to your host machine.