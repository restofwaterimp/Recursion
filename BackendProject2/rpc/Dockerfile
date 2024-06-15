#Chat program DockerFile

FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim \
    npm \ 
    nodejs
WORKDIR /opt
RUN wget https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh && \
sh Anaconda3-2024.02-1-Linux-x86_64.sh -b -p /opt/anaconda3 && \
rm -f Anaconda3-2024.02-1-Linux-x86_64.sh
ENV PATH /opt/anaconda3/bin:$PATH
RUN pip install --upgrade pip
RUN pip install Faker --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
RUN apt-get install  -y automake bison flex g++ git libboost-all-dev libevent-dev libssl-dev libtool make pkg-config
RUN npm install n -g
WORKDIR /
CMD bash
