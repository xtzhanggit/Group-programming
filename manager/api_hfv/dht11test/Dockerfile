FROM alpine:latest
MAINTAINER xtzhang<xtzhang@s-an.org>
WORKDIR /data
ENV TIME_ZONE Asia/Shanghai
COPY tcpclient.py /data
COPY tcpserver.py /data
COPY saveToMysql.py /data
COPY pydb.py /data
COPY pyfunc.py /data
COPY updateDevice.py /data
COPY entrypoint.sh /data
RUN apk --update add python3 py3-pip tzdata
RUN pip3 install pymysql
RUN echo "${TIME_ZONE}" > /etc/timezone \
&& ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime 
CMD python3 tcpserver.py
