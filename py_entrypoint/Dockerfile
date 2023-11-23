# Use Alpine Linux as the base image
FROM alpine:latest

LABEL maintainer="Your Name <your.email@example.com>"

ENV INSTALLED_TOOLS="\
    python3 \
    py3-pip \
    iputils-ping \
    net-tools \
    netcat-openbsd \
    openssh-client \
    busybox-extras \
    tmux \
    socat \
    git \
    vim \
    nano \
    curl \
    wget \
    bind-tools \
    jq \
    bash"



RUN apk update && \
    apk add --no-cache $INSTALLED_TOOLS && \
    rm -rf /var/cache/apk/*

RUN pip3 install Flask

WORKDIR /workspace

RUN printf "#!/bin/bash\n\
echo '-=-=-=-=-DEVOPS_TOOLS-=-=-=-=-\n\nHi there, good to see you!\n\nInstalled tools:\n $INSTALLED_TOOLS'\n\
exec /bin/bash" > /workspace/installed_tools_readme.log

COPY entrypoint.py .

RUN chmod +x entrypoint.py

ENTRYPOINT ["python3", "./entrypoint.py"]