FROM python:3.4

MAINTAINER joliu<joliu@s-an.org>

RUN pip3 install tensorflow -i https://pypi.douban.com/simple
RUN pip3 install numpy -i https://pypi.douban.com/simple
RUN pip3 install pymysql -i https://pypi.douban.com/simple
WORKDIR /data
COPY CGN/ /data

CMD python3 /data/interface.py


