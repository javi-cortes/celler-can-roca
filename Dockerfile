FROM python:3.11-rc-alpine

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

ENV PYTHONBUFFERED=1

COPY . /app

CMD ["python", "can_roca.py"]
