FROM python:3.6 

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
WORKDIR /  

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY scraper.py ./
COPY config.py ./

CMD python ./scraper.py && \
    celery -A scraper worker --concurrency $THREADS