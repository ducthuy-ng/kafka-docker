FROM kafka-base:1.1

# Overwrite existing configuration files
COPY ./*.properties ./conf/

RUN mkdir /var/lib/zookeeper && \
    echo "2" > /var/lib/zookeeper/myid