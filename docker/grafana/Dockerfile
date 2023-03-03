FROM grafana/grafana:9.3.6

# Set grafana password & influxdb token
ENV GF_SECURITY_ADMIN_PASSWORD=grafana
ENV GF_USERS_ALLOW_SIGN_UP=false
ENV INFLUXDB_TOKEN=secret-token
# ENV INFLUXDB_IP (already set in the Vagrantfile)

# Set timezone
ENV TZ=CET-1

# Copy grafana configuration files
COPY ./provisioning/ /etc/grafana/provisioning/
COPY ./grafana.ini /etc/grafana/grafana.ini