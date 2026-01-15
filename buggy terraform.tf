# main.tf - Terraform configuration with bugs

# Minor bug: Incorrect region name (should be "us-east-1" or similar)
provider "aws" {
  region = "east-us-1" 
}

# Major bug: Missing required 'ami' and 'instance_type' for the EC2 instance
resource "aws_instance" "web_server" {
  tags = {
    Name = "BuggyWebServer"
  }
  # Major bug: No security group attached, making it publicly accessible without firewall
  # Major bug: No key pair specified, making it impossible to SSH
}

# Minor bug: Incorrect syntax for output (missing value)
output "instance_ip" {
  description = "The public IP address of the web server"
  # value = aws_instance.web_server.public_ip
}
