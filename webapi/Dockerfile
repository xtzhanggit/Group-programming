FROM opengn.org:32333/alpine

MAINTAINER joliu<joliu@s-an.org>

COPY requirement.txt requirement.txt

RUN apk --update add python py-pip

RUN pip install -r requirement.txt 

RUN pip install flask-cors -i https://pypi.douban.com/simple
RUN mkdir webAPI

ADD webAPI/ webAPI/

CMD python webAPI/app.py
