resource "google_sql_database_instance" "inventory-db" {
  name             = "inventory-db"
  database_version = "POSTGRES_15"
  region           = "eu-west2"

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = "db-f1-micro"
  }
}
