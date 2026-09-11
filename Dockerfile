FROM python:3.11-slim
#Use the official Python runtime image as baseline kitchen
WORKDIR /app
#Establish active working directopry in container
COPY auditor.py .
#Copy script to container
CMD ["python", "auditor.py"]
#Define execution command to run container