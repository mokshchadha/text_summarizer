# text_summarizer

# project setup

Step 1 :- need to setup local virtual environment for python to store the CNN
`python3 -m venv venv ` #creates the venv
`source venv/bin/activate` #activates the venv
`pip3 install transformers` #requirement for the bart cnn
`pip3 install flask` #requirements for the server

additional set up for LLM
`pip3 install torch` #requirements for the mistril7b

Step 2:-
server setup for the flask server
`pip3 install gunicorn`
`gunicorn --bind 0.0.0.0:8000 server:app`
