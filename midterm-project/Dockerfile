FROM python:3.7.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["predict-midterm.py", "model_C=1.0.bin","./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn" ,"--bind=0.0.0.0:9696", "predict-midterm:app"]