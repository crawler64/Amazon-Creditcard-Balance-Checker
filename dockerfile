FROM joyzoursky/python-chromedriver:2.7-alpine3.7-selenium


RUN apk update
RUN apk add git
RUN git clone https://github.com/crawler64/Amazon-Creditcard-Balance-Checker.git

# Add your custom settings to the docker container
ADD config.ini ./Amazon-Creditcard-Balance-Checker/

CMD [ "python", "/Amazon-Creditcard-Balance-Checker/cc.py" ]
