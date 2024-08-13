[![Static testing](https://github.com/scottmacleod317/kitchen-inventory/actions/workflows/static-testing.yaml/badge.svg)](https://github.com/scottmacleod317/kitchen-inventory/actions/workflows/static-testing.yaml)
[![Deploy](https://github.com/scottmacleod317/kitchen-inventory/actions/workflows/deploy.yaml/badge.svg)](https://github.com/scottmacleod317/kitchen-inventory/actions/workflows/deploy.yaml)

# Kitchen Inventory
Kitchen Inventory is a simple application for helping you keep track of what food you have in your kitchen.

This repository contains the API and database.

API: FastAPI deployed to GCP as a Cloud Run service.

Database: Deployed to GCP as a Cloud SQL Postgres database.

# CI/CD
[GCP resource deployment](.github/workflows/deploy.yaml)
* Docker image to Artifact registry
* Cloud Run Service using the Docker image
* Cloud SQL Database

[Static analysis](.github/workflows/static-testing.yaml)
* pre-commit (containing `terraform_docs`, `terraform_fmt`, `terraform_tfsec`, `black`, `bandit`, `flake8`)


# Terraform docs
[Terraform README.md](terraform/README.md)

# Database migrations
For any updates to the database (schema or models), you need to create a migration with Alembic so that the changes in code are reflected in the database.

To do this, you need to follow these steps:
1. Authenticate with GCP (activate a service account with permissions and get an identity token)
2. Connect to the database with Cloud SQL Auth Proxy. See GCP docs [here](https://cloud.google.com/sql/docs/postgres/sql-proxy)
3. Run the migration to generate a migration script `alembic -c revision --autogenerate -m 'descriptive message here'`
4. Update the database `alembic upgrade head`
