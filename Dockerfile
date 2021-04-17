FROM python:3

#RUN git clone https://github.com/tbalson/cpu_test.git

WORKDIR predict_test/
COPY . /predict_test

#RUN git pull


EXPOSE 8080

RUN pip install -r requirements.txt

CMD ["make", "start"]
