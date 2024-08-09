# The Quote Getter

This lambda function should run on a schedule; every five minutes. When it runs it will grab three random quotes from the `quotable.io` API and saves them to an S3 bucket in JSON format.

## Deployment Instructions

1. Make sure you are in the `3-cloud` subdirectory.
2. Type `make requirements`
3. `make dev-setup`
4. `make run-checks`
5. `terraform init`
6. `terraform plan`
7. `terraform apply`

