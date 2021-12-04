# S3 bucket to store your Terraform tfstates
terraform {
  backend "s3" {
    bucket = "cr-pkp-keys"
    key    = "terraform-matadata/terraform.tfstates" # KEY must be unique for each PROJECT
  }
}

# ACCOUNT A
# BUCKET_1_TFSTATES
# - project1/tfstates
# - project2/tfstates
# - ...