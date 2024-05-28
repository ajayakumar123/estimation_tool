## Objective: 
To develop a tool that estimates effort based on historical data using Flask and MongoDB.

## Key Features:
User registration and authentication
Task estimation submission
Effort calculation based on historical data
Data storage and retrieval in MongoDB

## Techonlogies used:
Front-End: HTML, CSS, JavaScript, Jinja2,Bootstrap,AJAX
Back-End: Python(Flask),API
Database: MongoDB
Tools: Github, Postman,Docker, Jenkins (for CI/CD)

## steps to run application:
=======================

clone the repository: git clone https://github.com/ajayakumar123/estimation_tool.git

change project directory: cd estimation_tool

Run docker compose to build the dockerimages(containers):estimation_tool>docker-compose up -d --build

TO down(stop) docker compose : estimation_tool>docker compose down


## In local with virtual venv(optional):

Clone Repository: $ git clone https://github.com/ajayakumar123/estimation_tool.git

Create & Activate Virtualenv: $ cd <app_root>  python3 -m venv venv $ venv/scripts/activate

Install Dependencies: (venv) $ pip install -r requirements.txt

Run application : (venv) $ python run.py



