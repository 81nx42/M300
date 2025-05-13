# Login
Connect-AzAccount

# Variablen
$resourceGroup = "m300-projekt-rg"
$location = "westeurope"
$appServicePlan = "m300-app-plan"
$webApp = "m300-inventar-api"
$sqlServer = "m300sqlserver123"
$sqlDb = "InventarDB"

# Ressourcengruppe
New-AzResourceGroup -Name $resourceGroup -Location $location

# App Service Plan
New-AzAppServicePlan -Name $appServicePlan -Location $location -ResourceGroupName $resourceGroup -Tier "Free"

# Web App
New-AzWebApp -Name $webApp -Location $location -AppServicePlan $appServicePlan -ResourceGroupName $resourceGroup

# SQL Server & DB
New-AzSqlServer -ResourceGroupName $resourceGroup -ServerName $sqlServer -Location $location -SqlAdministratorCredentials (Get-Credential)
New-AzSqlDatabase -ResourceGroupName $resourceGroup -ServerName $sqlServer -DatabaseName $sqlDb -RequestedServiceObjectiveName "Basic"
