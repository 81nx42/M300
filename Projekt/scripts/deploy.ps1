# Variablen
$resourceGroup = "m300-projekt-rg-v2"
$location = "westeurope"
$appServicePlan = "m300-app-plan-v2"
$webApp = "m300-inventar-api-v2"

# Login (nur beim ersten Mal)
Connect-AzAccount

# Ressourcengruppe
New-AzResourceGroup -Name $resourceGroup -Location $location -ErrorAction SilentlyContinue

# App Service Plan
New-AzAppServicePlan -Name $appServicePlan -Location $location -ResourceGroupName $resourceGroup -Tier Free -ErrorAction SilentlyContinue

# Web App
New-AzWebApp -Name $webApp -Location $location -AppServicePlan $appServicePlan -ResourceGroupName $resourceGroup
