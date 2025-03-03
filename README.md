This project is designed to send emails asynchronously using **Celery** and **Redis** as the task queue backend.

Clone the repository

Set up a virtual environment and activate

pip install -r requirements.txt

Create a .env file in the project root and add the most protected things that don't want to show others

after that run the migrations

Install Redis and Start Redis Server

Install Celery and Start Celery Worker

both Redis and Celery is in the requirement but you should have to start the server

endpoints ==> 1)  http://127.0.0.1:8000/emails/   
              2)  http://127.0.0.1:8000/emails/trigger-email-task/





