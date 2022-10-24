terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
}
provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "KPMG21_JosephFernandes_ProjectExercise"
}
resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}
resource "azurerm_linux_web_app" "main" {
  name                = "joefernandestodoapp${var.prefix}"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id
  site_config {
    application_stack {
      docker_image     = "josephfernandes14/todoapp"
      docker_image_tag = "latest"
    }
  }
  app_settings = {

    "FLASK_APP"                  = "todo_app / app"
    "FLASK_ENV"                  = "development"
    "SECRET_KEY"                 = "secret-key"
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "CONNECTION_STRING"          = azurerm_cosmosdb_account.db.connection_strings[0]
    "DATABASE"                   = "todo_app"
    "COLLECTION"                 = "todo_tasks"
    "CLIENTSECRET"               = var.client_secret
    "CLIENTID"                   = var.client_id
  }
}


resource "azurerm_cosmosdb_account" "db" {
  name                = "joaccount-cosmos-db-${var.prefix}"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }
  capabilities {
    name = "EnableServerless"
  }

  capabilities {
    name = "EnableMongo"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}


resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "josephtodoapp-cosmos-mongo-db-${var.prefix}"
  resource_group_name = data.azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.db.name

  # lifecycle {
  #   prevent_destroy = true
  # }
}
resource "azurerm_storage_account" "main" {
  name                     = "tfstateb3eqk"
  resource_group_name      = data.azurerm_resource_group.main.name
  location                 = data.azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"


  tags = {
    environment = "staging"
  }
}

resource "azurerm_storage_container" "tfstate" {
  name                  = "tfstatecontainer"
  storage_account_name  = azurerm_storage_account.main.name
  container_access_type = "blob"
}
