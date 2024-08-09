
resource "aws_cloudwatch_log_group" "app_logs" {
  name = "/app/logs"
}

resource "aws_cloudwatch_log_metric_filter" "great_quote_filter" {
  name           = "GreatQuoteFilter"
  pattern        = "\"[GREAT QUOTE]\""
  log_group_name = aws_cloudwatch_log_group.app_logs.name

  metric_transformation {
    name      = "GreatQuoteCount"
    namespace = "GreatQuotes"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "great_quote_alarm" {
  alarm_name          = "GreatQuoteAlarm"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = "GreatQuoteCount"
  namespace           = "GreatQuotes"
  period              = 60
  statistic           = "Sum"
  threshold           = 1

  alarm_description = "Great quote detected!"
  alarm_actions     = [aws_sns_topic.email_topic.arn]
}

resource "aws_sns_topic" "email_topic" {
  name = "GreatQuoteEmailTopic"
}


resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.email_topic.arn
  protocol  = "email"
  endpoint  = "ellybalci@gmail.com"
}

# alex.swain@northcoders.com