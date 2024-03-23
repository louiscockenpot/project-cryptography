FROM python:3.9-slim

WORKDIR /app

COPY templates /app/templates

COPY app.py elGamalSign.py elGamalVerify.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

