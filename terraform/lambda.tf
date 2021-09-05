provider "aws" {
  region = "us-west-2"
  profile = "home"
}

resource "aws_iam_role" "tamagotchi" {
  name = "iam_for_tamagotchi"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "lambda_logging_policy" {
	role = aws_iam_role.tamagotchi.name
	policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_s3_policy" {
	role = aws_iam_role.tamagotchi.name
	policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}



variable "TW_ACCESS_TOKEN" {
	type = string
}
variable "TW_ACCESS_TOKEN_SECRET" {
	type = string
}
variable "TW_API_KEY" {
	type = string
}
variable "TW_API_KEY_SECRET" {
	type = string
}

resource "aws_lambda_function" "tamagotchi" {
	filename = "tweet_lambda.zip"
	function_name = "tweet_lambda"
	role = aws_iam_role.tamagotchi.arn
	handler = "tweet.lambda_main"

	source_code_hash = filebase64sha256("tweet_lambda.zip")

	runtime = "python3.9"
	timeout = 120

	environment {
		variables = {
			TW_ACCESS_TOKEN = var.TW_ACCESS_TOKEN,
			TW_ACCESS_TOKEN_SECRET = var.TW_ACCESS_TOKEN_SECRET,
			TW_API_KEY = var.TW_API_KEY,
			TW_API_KEY_SECRET = var.TW_API_KEY_SECRET,
		}
	}
}

resource "aws_cloudwatch_event_rule" "cronjob" {
	name = "trigger_lambda"
	description = "Triggers lambda based on cron schedule"
	schedule_expression = "cron(0 12 * * ? *)"
}

resource "aws_cloudwatch_event_target" "tamagotchi_lambda_schedule" {
	rule = "${aws_cloudwatch_event_rule.cronjob.name}"
	target_id = "tamagotchi"
	arn = "${aws_lambda_function.tamagotchi.arn}"
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_lambda" {
	statement_id = "AllowExecutionFromCloudWatch"
	action = "lambda:InvokeFunction"
	function_name = "${aws_lambda_function.tamagotchi.function_name}"
	principal = "events.amazonaws.com"
	source_arn = "${aws_cloudwatch_event_rule.cronjob.arn}"
}