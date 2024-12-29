# BERT based Spam Detection Web Application
- Developed a RESTful API using Flask to integrate BERT classification model.
- BERT model fine tuned for spam detection task in Spam_filter_Thesis and there is available on https://huggingface.co/vsak

# Download the models and save them locally
- Run load_model.py script

#  Build a multicontainer architecture with Docker
- Base app runs on 5000 port and models API runs on 5001 port.
- Build the base image that has the requirements. Run docker build -t base-image:latest . 
- Run docker compose up, to build the multicontainer app.
