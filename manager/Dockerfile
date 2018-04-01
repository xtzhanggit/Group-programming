FROM python:3.4
MAINTAINER joliu<joliu@s-an.org>
RUN pip3 install pymysql -i https://pypi.douban.com/simple
WORKDIR /data
COPY api/ /data
CMD python3 hfv.py
