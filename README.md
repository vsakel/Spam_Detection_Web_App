# BERT based Spam Detection Web Application
- Developed a RESTful API using Flask to integrate BERT classification model.
- Used BERT models, that fine tuned for spam detection task in Development of Spam Filters Using Artificial Intelligence Techniques Thesis and there are available on https://huggingface.co/vsak

# Download the models and save them locally
- Run load_model.py script

#  Build a multicontainer architecture with Docker
- docker compose tool
- Base app (frontend) runs on 5000 port and models API runs on 5001 port.
- Build the base image that has the requirements. Run docker build -t base-image:latest . 
- Run docker compose up, to build the multicontainer app.
