FROM opengn.org:32333/easypi/alpine-arm
MAINTAINER joliu<joliu@s-an.org>
WORKDIR /data
RUN apk --update add python3
COPY tcpOffclient.py /data
COPY tcpOnclient.py /data
COPY tcpserver.py /data
COPY status.db /data
CMD python3 /data/tcpserver.py
