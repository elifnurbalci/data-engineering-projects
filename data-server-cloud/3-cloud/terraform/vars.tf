variable "data_bucket_prefix" {
  type = string
  default = "nc-demo-de-quotes"
}

variable "code_bucket_prefix" {
  type = string
  default = "nc-demo-de-code"
}

variable "lambda_name" {
  type = string
  default = "quote_handler"
}

variable "python_runtime" {
  type = string
  default = "python3.12"
}

variable "s3_bucket_name" {
  type = string
  default = "nc-elly-tf-demo-20240418102118956000000001"
}

variable "arn_name" {
  type = string
  default = "arn:aws:iam::975050367112:user/de-mar-elly"
}