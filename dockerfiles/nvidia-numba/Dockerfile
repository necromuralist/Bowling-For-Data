ARG IMAGE_NAME=nvidia/cuda
FROM ${IMAGE_NAME}:11.1-devel-ubuntu20.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV CUDNN_VERSION 8.0.5.39

LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libcudnn8=$CUDNN_VERSION-1+cuda11.1 \
    libcudnn8-dev=$CUDNN_VERSION-1+cuda11.1 \
    libcusolver10 \
    rsync \
    zile \
    openssh-server && \
    apt-mark hold libcudnn8 && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --create-home --shell /bin/bash bravo && \
    echo "export PATH=$PATH:/home/bravo/.local/bin/" && \
    echo "source /opt/conda/etc/profile.d/conda.sh" >> /home/bravo/.bashrc && \
    echo 'eval "$(register-python-argcomplete conda)"'

COPY authorized_keys /home/bravo/.ssh/
COPY setup_conda.sh /home/bravo/
COPY run_in_container.sh /run_in_container.sh
ENTRYPOINT service ssh restart && bash

