FROM python:3.7

RUN pip install requests
RUN pip install schedule
RUN pip install python-telegram-bot

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/pythonscriptcpit3.py