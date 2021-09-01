FROM python:3.8.0-buster

# Make a dir for application
WORKDIR /app

# Install dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "selfbot.py"]