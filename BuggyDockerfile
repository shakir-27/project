# Dockerfile with bugs

# Minor bug: Using an old base image (should be a more recent stable version)
FROM ubuntu:18.04

# Major bug: Running as root user, security vulnerability
USER root

WORKDIR /app

# Minor bug: Using ADD instead of COPY for local files
ADD . /app

# Major bug: Exposing a port that the application might not actually use
EXPOSE 8080

# Major bug: CMD instruction doesn't correctly start a typical web application
CMD ["echo", "Hello, Docker!"]
