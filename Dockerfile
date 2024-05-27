#python base image
FROM python:3.8-slim

#working directory
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app
# Install
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV FLASK_APP=app.py
# Run app.py
CMD ["flask", "run", "--host=0.0.0.0"]

