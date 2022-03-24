FROM kafka-base:1.1

# Overwrite existing configuration files
COPY ./* ./conf/

RUN mkdir /var/lib/zookeeper && \
    echo "1" > /var/lib/zookeeper/myid