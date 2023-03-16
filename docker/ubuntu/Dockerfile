FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

# Set influxdb token
ENV INFLUXDB_TOKEN=secret-token
# ENV INFLUXDB_IP (already set in the Vagrantfile)

# Set timezone
ENV TZ=CET-1

# Install dependencies & add telegraf repository
RUN apt-get update && apt-get install -y \
    locales \
    curl \
    lsb-release \
    openssh-server \
    sudo \
    nano \
    python3 \
    gnupg \
    apt-transport-https \
    && curl -s https://repos.influxdata.com/influxdata-archive_compat.key > influxdata-archive_compat.key \
    && echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c && cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null \
    && echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

# Install required additional packages
RUN apt-get install -y \
    iproute2 \
    mptcpize \
    iperf3 \
    iputils-ping \
    telegraf \
    git \
    cmake \
    build-essential \
    cargo \
    netcat \
    net-tools \
    ffmpeg \
    && apt remove rustc -y \
    && rm -rf /var/lib/apt/lists/*

# Ensure we have the fr_FR.UTF-8 locale available
RUN locale-gen fr_FR.UTF-8

# Setup the vagrant user
RUN if ! getent passwd vagrant; then useradd -d /home/vagrant -m -s /bin/bash vagrant; fi \
    && echo vagrant:vagrant | chpasswd \
    && echo 'vagrant ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && mkdir -p /etc/sudoers.d \
    && echo 'vagrant ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/vagrant \
    && chmod 0440 /etc/sudoers.d/vagrant

# Add the vagrant insecure public key
RUN mkdir -p /home/vagrant/.ssh \
    && chmod 0700 /home/vagrant/.ssh \
    && wget --no-check-certificate \
      https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub \
      -O /home/vagrant/.ssh/authorized_keys \
    && chmod 0600 /home/vagrant/.ssh/authorized_keys \
    && chown -R vagrant /home/vagrant/.ssh

USER vagrant

# Update rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && echo "source $HOME/.cargo/env" >> /home/vagrant/.bashrc \
    && echo "export DISPLAY=:1" >> /home/vagrant/.bashrc 

USER root

# Don't clean packages, we might be using vagrant-cachier
RUN rm /etc/apt/apt.conf.d/docker-clean

# Create the privilege separation directory for sshd
RUN mkdir -p /run/sshd

# Copy configuration files
COPY ./telegraf.conf /etc/telegraf/telegraf.conf

# Run sshd and telegraf in the foreground
CMD /usr/sbin/sshd -D \
    -o UseDNS=no\
    -o UsePAM=no\
    -o PasswordAuthentication=yes\
    -o PidFile=/tmp/sshd.pid & \
    /usr/bin/telegraf --config /etc/telegraf/telegraf.conf