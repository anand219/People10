FROM tomcat:latest

MAINTAINER anand

RUN apt-get update && apt-get -y upgrade && apt-get wget && \

    cd /usr/local/tomcat/webapps/ && wget https://master.dl.sourceforge.net/project/pebble/pebble/1.4.2/pebble-1.4.2.war

WORKDIR /usr/local/tomcat
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

CMD [ "catalina.sh", "run" ]



