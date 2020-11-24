FROM smirnou/watsor

USER root

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Add Bashio
ARG BASHIO_VERSION=0.9.0
RUN apt-get update && apt-get install -y --no-install-recommends \
        jq \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /tmp/bashio \
    && wget -q -O - https://github.com/hassio-addons/bashio/archive/v${BASHIO_VERSION}.tar.gz | tar -xzf - --strip 1 -C /tmp/bashio \
    && mv /tmp/bashio/lib /usr/lib/bashio \
    && ln -s /usr/lib/bashio/bashio /usr/bin/bashio \
    && rm -rf /tmp/bashio

WORKDIR /

COPY config.sh config.sh
COPY start.py start.py

#USER watsor    # https://github.com/home-assistant/supervisor/issues/2158#issuecomment-714370975

CMD ["python3", "-m", "start", \
     "--log-path", "/var/log/watsor", \
     "--config", "/etc/watsor/config.yaml", \
     "--model-path", "/usr/share/watsor/model"]

