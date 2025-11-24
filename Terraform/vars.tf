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

variable "master_username" {
  description = "Redshift master username"
  type        = string
}

variable "master_password" {
  description = "Redshift master password"
  type        = string
  sensitive   = true  
} 

variable "db_name" {
  description = "my_db"
  type        = string
} 

