build the image from docker file
docker build -t tomcat .
docker run -it --rm -p 9090:8080 tomcat
#after deploying the peddle war i have not validated the Docker file
my vagrant machine giving Error like below
[vagrant@localhost ~]$ sudo docker build -t tomcat .
Sending build context to Docker daemon 98.54 MB
Sending build context to Docker daemon
Step 0 : FROM tomcat:latest
Pulling repository tomcat
Get https://index.docker.io/v1/repositories/library/tomcat/images: dial tcp: lookup index.docker.io: Temporary failure in name resolution

I have tried restart the docker daemon but no luck i am hoping above task is good to go access
localhost:9090/peddle/

