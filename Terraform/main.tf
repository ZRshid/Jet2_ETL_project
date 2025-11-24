terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}
# Configure the AWS Provider
provider "aws" {
  region =  var.aws_region
} 

# TRUST POLICY DOCUMENT FOR REDSHIFT ROLE
data "aws_iam_policy_document" "redshift_trust" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["redshift.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

# IAM ROLE FOR REDSHIFT
resource "aws_iam_role" "redshift_role" {
  name               = "redshift-access-role"
  assume_role_policy = data.aws_iam_policy_document.redshift_trust.json
}

# S3 PERMISSIONS POLICY DOCUMENT
data "aws_iam_policy_document" "s3_policy" {
  statement {
    effect    = "Allow"
    actions   = ["s3:GetObject", "s3:ListBucket"]
    resources = [
      aws_s3_bucket.processed_data_bucket.arn,
      "${aws_s3_bucket.processed_data_bucket.arn}/*"
    ]
  }
}

# ATTACH INLINE POLICY TO REDSHIFT ROLE
resource "aws_iam_role_policy" "redshift_s3_policy" {
  name   = "RedshiftS3AccessPolicy"
  role   = aws_iam_role.redshift_role.id
  policy = data.aws_iam_policy_document.s3_policy.json
}

resource "aws_redshift_cluster" "redshift" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = var.db_name
  master_username    = var.master_username
  master_password    = var.master_password
  node_type          = "ra3.xlplus"
  cluster_type       = "single-node"
  iam_roles          = [aws_iam_role.redshift_role.arn]
  skip_final_snapshot = true
}
