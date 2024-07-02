
# Terraform AWS S3 Bucket Configuration

## Overview

This Terraform configuration creates an AWS S3 bucket and configures its public access settings to enhance the security of the bucket.

## Terraform Configuration

The configuration starts with the `terraform` block, which specifies the required provider. In this case, the `hashicorp/aws` provider is used.

```hcl
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}
```

The `provider` block sets the AWS region to "ap-southeast-2".

```hcl
provider "aws" {
  region = "ap-southeast-2"
}
```

The `aws_s3_bucket` resource creates an S3 bucket, but no specific configuration is provided for the bucket.

```hcl
resource "aws_s3_bucket" "S3Bucket" {
}
```

The `aws_s3_bucket_public_access_block` resource configures the public access settings for the S3 bucket. It sets the following options:

- `block_public_acls`: Blocks public access to the bucket's ACLs.
- `block_public_policy`: Blocks public access to the bucket's policy.
- `ignore_public_acls`: Ignores public ACLs for the bucket.
- `restrict_public_buckets`: Restricts public access to the bucket.

```hcl
resource "aws_s3_bucket_public_access_block" "example" {
  bucket = aws_s3_bucket.S3Bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

These settings help to enhance the security of the S3 bucket by preventing unauthorized public access to the bucket and its contents.
