FROM nvidia/cuda:11.0-base-ubuntu20.04 as cuda-base
ENV DEBIAN_FRONTEND=noninteractive
# Install some basic utilities
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
 && rm -rf /var/lib/apt/lists/*



# Install python 3.8


RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install python3-pip python3.8-dev python3.8-distutils python3.8-venv -y

# Make Python3 default by making a virtual env. Its a bad idea to overwrite system python
RUN python3.8 -m venv /venv
ENV PATH=/venv/bin:$PATH


FROM cuda-base as dl-requirements
RUN pip install wheel
RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html \
    && pip install --upgrade jax jaxlib==0.1.57+cuda110 -f https://storage.googleapis.com/jax-releases/jax_releases.html \
    && rm -rf /var/lib/apt/lists/*

#RUN mkdir requirements-tests
#COPY test_pytorch.py requirements-tests/.


FROM dl-requirements as requirements-base 
COPY requirements.txt .
RUN pip install -r requirements.txt 

FROM dl-requirements as jupyter


RUN pip install jupyterlab

RUN mkdir /basin
WORKDIR /basin
