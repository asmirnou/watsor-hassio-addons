FROM smirnou/watsor.pi3

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Add Bashio
ARG BASHIO_VERSION=0.9.0
RUN install_packages \
        jq \
    && mkdir -p /tmp/bashio \
    && wget -q -O - https://github.com/hassio-addons/bashio/archive/v${BASHIO_VERSION}.tar.gz | tar -xzf - --strip 1 -C /tmp/bashio \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    && rm -rf /tmp/bashio

WORKDIR /

COPY config.sh config.sh
COPY start.py start.py

CMD ["python3", "-m", "start", \
     "--log-path", "/var/log/watsor", \
     "--config", "/etc/watsor/config.yaml", \
     "--model-path", "/usr/share/watsor/model"]

