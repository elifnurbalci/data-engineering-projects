resource "aws_s3_bucket" "demo_bucket" {
  bucket_prefix = "nc-elly-tf-demo-"

  tags = {
    Name = "nc-elly-tf-demo"
    Environment = "Dev"
  }
}

resource "aws_s3_object" "demo_object" {
  bucket = "nc-elly-tf-demo-20240418102118956000000001"
  key = "test_file.txt"
  source = "test_file.txt"
}
