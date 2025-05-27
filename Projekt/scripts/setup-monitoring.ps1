$resourceGroup = "m300-projekt-rg-v2"
$webApp = "m300-inventar-api-v2"
$appInsightsName = "m300-appinsights-noah-v2"

# App Insights erstellen
$insights = New-AzApplicationInsights -ResourceGroupName $resourceGroup -Name $appInsightsName -Location "westeurope" -Kind web

# Web App mit App Insights verknüpfen
Set-AzWebApp -ResourceGroupName $resourceGroup -Name $webApp -AppSettings @{ "APPINSIGHTS_INSTRUMENTATIONKEY" = $insights.InstrumentationKey }
