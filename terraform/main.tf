terraform {
  # Security: Use a remote backend for state management
  # backend "s3" {
  #   bucket         = "your-terraform-state-bucket"
  #   key            = "aiotorrent-app/terraform.tfstate"
  #   region         = "us-east-1"
  #   encrypt        = true
  #   dynamodb_table = "your-terraform-state-lock-table"
  # }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  # Security: Use IAM roles for authentication in production, not access keys
}

# Security: Create a dedicated security group with least privilege
resource "aws_security_group" "app_sg" {
  name        = "${var.project_name}-sg"
  description = "Allow SSH and HTTP/Flask traffic"
  vpc_id      = var.vpc_id

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["your.trusted.ip.range/32"] # Restrict this to known IPs in production
  }

  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Security: Restrict this to known IPs in production
  }

  ingress {
    description = "Flask app port from anywhere"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Security: Restrict this to known IPs in production
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-sg"
  }
}

# Security: Create an SSH key pair for instance access
resource "aws_key_pair" "app_key" {
  key_name   = "${var.project_name}-key"
  public_key = var.public_key
}

# Simulate an EC2 instance for demonstration purposes
resource "aws_instance" "app_instance" {
  ami           = var.ami_id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  vpc_security_group_ids = [aws_security_group.app_sg.id]
  key_name               = aws_key_pair.app_key.key_name

  tags = {
    Name = "${var.project_name}-instance"
  }

  # Security: Use remote-exec for initial setup, but prefer cloud-init or user data
  # provisioner "remote-exec" {
  #   inline = [
  #     "sudo apt update -y",
  #     "sudo apt install -y python3-pip",
  #     "pip3 install docker-compose"
  #   ]
  # }
}

output "instance_public_ip" {
  description = "The public IP address of the EC2 instance"
  value       = aws_instance.app_instance.public_ip
}

output "instance_private_ip" {
  description = "The private IP address of the EC2 instance"
  value       = aws_instance.app_instance.private_ip
}
