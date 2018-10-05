FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-add-repository universe -y
RUN apt-get install default-jdk -y
RUN update-alternatives --config java
RUN apt-get install maven -y
RUN apt-get update -y

WORKDIR /usr/src/app
CMD ["scripts/run.sh"]
