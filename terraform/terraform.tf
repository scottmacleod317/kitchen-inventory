terraform {
  backend "gcs" {
    bucket = "kitchen-inv-tf-state"
    prefix = "terraform/state"
  }

  required_version = "~> 1.9.2"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.40.0"
    }
  }
}

provider "google" {
  project = var.project
  region  = "europe-west2"
}
