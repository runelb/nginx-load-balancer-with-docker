FROM python:3
COPY ./libraries.txt /libraries.txt
WORKDIR /
RUN pip install -r libraries.txt
COPY . /
ENTRYPOINT [ "python3" ]
CMD [ "app3.py" ]