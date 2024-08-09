data "archive_file" "lambda" {
  type        = "zip"
  output_file_mode = "0666"
  source_file = "${path.module}/../src/quotes.py"
  output_path = "${path.module}/../function.zip"
}

data "archive_file" "layer" {
  type = "zip"
  output_file_mode = "0666"
  source_dir = "${path.module}/../layer/"
  output_path = "${path.module}/../layer.zip"
}

resource "aws_lambda_function" "quote_handler" {
    function_name = "${var.lambda_name}"
    s3_bucket = aws_s3_bucket.code_bucket.bucket
    s3_key = "quotes/function.zip"
    role = aws_iam_role.lambda_role.arn
    handler = "quotes.lambda_handler"
    runtime = var.python_runtime
    timeout = 60
    layers = [aws_lambda_layer_version.requests_layer.arn]
    environment {
      variables = {
        S3_BUCKET_NAME = var.s3_bucket_name
      }
    }
}

resource "aws_lambda_permission" "allow_eventbridge" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.quote_handler.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.scheduler.arn
  source_account = data.aws_caller_identity.current.account_id
}

resource "aws_lambda_layer_version" "requests_layer" {
  layer_name = "requests_layer"
  compatible_runtimes = [var.python_runtime]
  s3_bucket = aws_s3_bucket.code_bucket.bucket
  s3_key = "quotes/layer.zip"
}