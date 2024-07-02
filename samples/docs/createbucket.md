
# AWS CloudFormation Template: S3 Bucket Creation

## Overview

This CloudFormation template demonstrates the creation of an S3 bucket, a popular cloud storage service provided by Amazon Web Services (AWS).

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Demo of S3 bucket creation

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
```

The key elements of this template are:

1. **AWSTemplateFormatVersion**: This specifies the version of the CloudFormation template format, which is '2010-09-09' in this case.
2. **Description**: A brief description of the purpose of the template, which is to create an S3 bucket.
3. **Resources**: This section defines the AWS resources that will be created by the template. In this case, it defines a single S3 bucket resource.

When this template is deployed, it will create an S3 bucket in the user's AWS account.
