resource "aws_cloudwatch_event_rule" "scheduler" {
  name                = "FiveMinuteSchedule"
  description         = "Schedule for triggering Lambda every 5 minutes"
  schedule_expression = "rate(5 minutes)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.scheduler.name
  target_id = "LambdaTarget"
  arn       = aws_lambda_function.quote_handler.arn
}
