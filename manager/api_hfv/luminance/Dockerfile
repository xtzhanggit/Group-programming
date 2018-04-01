FROM opengn.org:32333/easypi/alpine-arm
MAINTAINER joliu<joliu@s-an.org>
RUN apk --update add python3 py3-pip tzdata
RUN pip3 install pymysql -i https://pypi.douban.com/simple
RUN echo "${TIME_ZONE}" > /etc/timezone \
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime 
WORKDIR /data
ENV TIME_ZONE Asia/Shanghai
COPY tcpclient.py /data
COPY tcpserver.py /data
COPY saveToMysql.py /data

CMD python3 /data/tcpserver.py
