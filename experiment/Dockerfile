# FROM ubnt/selenium-chrome-standalone
FROM python:3.10-slim

COPY requirements.txt requirements.txt

# RUN apt-get update && apt-get install -yq \
#     chromium-browser 


# chromeDriver v2.35
# RUN wget -q "https://chromedriver.storage.googleapis.com/100.0.4896.20/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
#     && unzip /tmp/chromedriver.zip -d /usr/bin/ \
#     && rm /tmp/chromedriver.zip

# RUN /bin/sh -c apt-get install -yq \
#     python-pip

RUN  pip install --no-cache-dir -r requirements.txt

WORKDIR /home/app

COPY ./ /home/app/

# CMD ["python", "main.py"]
