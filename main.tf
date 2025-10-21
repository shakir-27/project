provider "aws" {
  region = "us-east-10" # Major bug: Invalid AWS region
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-terraform-bucket-12345"
  acl    = "private"

  tags = {
    Name        = "My Terraform S3 Bucket"
    Environment = "Dev"
  }
}
