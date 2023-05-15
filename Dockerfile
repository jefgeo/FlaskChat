FROM python:3.10-alpine

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5999
CMD [ "python", "-m" , "flask", "run"]

