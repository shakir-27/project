variable "aws_region" {
  description = "AWS region for resource deployment"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
  default     = "ami-0abcdef1234567890" # Replace with a valid AMI ID for your region
}

variable "public_key" {
  description = "SSH public key to be placed on the instance"
  type        = string
  sensitive   = true # Security: Mark as sensitive to prevent logging
}

variable "vpc_id" {
  description = "ID of the VPC to deploy into"
  type        = string
  # default = "vpc-0abcdef1234567890" # Uncomment and set if you have a specific VPC
}

variable "subnet_id" {
  description = "ID of the subnet to deploy into"
  type        = string
  # default = "subnet-0abcdef1234567890" # Uncomment and set if you have a specific subnet
}

variable "project_name" {
  description = "Name of the project for tagging resources"
  type        = string
  default     = "aiotorrent-app"
}
