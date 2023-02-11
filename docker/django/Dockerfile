FROM python:3.10.6-slim

WORKDIR /demo_project

RUN ls -l .

COPY . .

RUN ls -l ./demo_project

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED 1

CMD ["python", "./demo_project/manage.py", "runserver", "0.0.0.0:8000"]