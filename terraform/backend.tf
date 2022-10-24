terraform {
  backend "azurerm" {
    resource_group_name  = "KPMG21_JosephFernandes_ProjectExercise"
    storage_account_name = "tfstateb3eqk"
    container_name       = "tfstatecontainer"
    key                  = "demotf.terraform.tfstate"
  }
}
