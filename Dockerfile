FROM python:3.6-alpine

RUN adduser -D intranet_2

WORKDIR /home/intranet_2


COPY requirements.txt requirements.txt

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt


RUN venv/bin/pip install gunicorn pymysql
RUN pip install "pymysql<0.9"

COPY app app
COPY migrations migrations
COPY intranet.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP intranet.py

RUN chown -R intranet_2:intranet_2 ./
USER intranet_2

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

