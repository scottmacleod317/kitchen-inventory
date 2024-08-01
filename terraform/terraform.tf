terraform {
  backend "gcs" {
    bucket  = "kitchen-inv-tf-state"
    prefix  = "terraform/state"
  }

  required_version = "~> 1.9.2"
}

provider "google" {
  project     = var.project
  region      = "europe-west2"
}
