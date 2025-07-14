
resource "aws_s3_bucket" "raw_data_bucket" {
  bucket = var.raw_data_bucket
  force_destroy= true
  tags = {
    Name = "raw_data_bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket" "processed_data_bucket" {
  bucket = var.processed_data_bucket
  force_destroy= true
  tags = {
    Name = "processed_data_bucket"
    Environment = "Dev"
  }
}





