FROM python:3.12-slim

WORKDIR /portfolio

COPY app.py requirements.txt static templates /portfolio/
COPY static /portfolio/static
COPY templates /portfolio/templates

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
