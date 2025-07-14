variable "raw_data_bucket" {
  description = "raw data bucket"
  type        = string
  default     = "raw-data"
}

# Name of the S3 bucket used for storing processed data from the raw_data bucket.
variable "processed_data_bucket" {
  description = "processed data bucket"
  type        = string
  default     = "processed-data"
}

variable "aws_region" {
  description = "the aws region to deploy in"
  default     = "eu-west-2"
}