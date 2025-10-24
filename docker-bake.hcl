variable "DOCKER_REGISTRY" {
  default = "your-docker-registry.com"
}

variable "IMAGE_NAME" {
  default = "aiotorrent-flask-app"
}

variable "IMAGE_TAG" {
  default = "latest"
}

target "default" {
  dockerfile = "./app/Dockerfile"
  context    = "."
  tags = [
    "${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}",
    "${DOCKER_REGISTRY}/${IMAGE_NAME}:{{date "20060102"}}-{{.VCS.Commit.Short}}"
  ]
  platforms = [
    "linux/amd64"
  ]
  # Security: Ensure build arguments are not exposing sensitive information
  # args = {
  #   "HTTP_PROXY" = "http://proxy.example.com"
  # }
}
