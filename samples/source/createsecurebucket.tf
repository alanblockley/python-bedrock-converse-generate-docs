terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_s3_bucket" "S3Bucket" {

}

resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.S3Bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}