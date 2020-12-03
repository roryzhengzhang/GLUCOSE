FROM python:3.5-buster

ENV FLASK_APP="app:app"

WORKDIR /wesbite

EXPOSE 5000
#run command once at build time
COPY requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
#RUN python website/download_model.py 774M
#run CMD when the container starts
CMD ["flask", "run", "--host", "0.0.0.0"]