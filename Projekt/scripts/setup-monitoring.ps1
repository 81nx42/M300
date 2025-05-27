# === Konfiguration ===
$resourceGroup = "m300-projekt-rg"
$webApp = "m300-inventar-api"         # Passe an, falls dein App Service anders heißt
$appInsightsName = "m300-appinsights-noah"
$actionGroupName = "m300-alerts"
$email = "noah.scheidegger@edu.tbz.ch"    # Deine echte E-Mail

# === Application Insights ===
$insights = Get-AzApplicationInsights -ResourceGroupName $resourceGroup -Name $appInsightsName -ErrorAction SilentlyContinue
if (-not $insights) {
    Write-Host "App Insights wird erstellt..."
    $insights = New-AzApplicationInsights -ResourceGroupName $resourceGroup -Name $appInsightsName -Location "westeurope" -Kind web
} else {
    Write-Host "App Insights existiert bereits: $appInsightsName"
}

# === Web App mit App Insights verknüpfen ===
if ($insights.InstrumentationKey) {
    Set-AzWebApp -ResourceGroupName $resourceGroup -Name $webApp -AppSettings @{"APPINSIGHTS_INSTRUMENTATIONKEY" = $insights.InstrumentationKey}
    Write-Host "Web App $webApp mit App Insights verknüpft."
} else {
    Write-Host "Achtung: Kein InstrumentationKey gefunden. Prüfe App Insights im Azure-Portal!"
}

# === Action Group erstellen (E-Mail-Alert) ===
$actionGroup = Get-AzActionGroup -ResourceGroupName $resourceGroup -Name $actionGroupName -ErrorAction SilentlyContinue
if (-not $actionGroup) {
    $actionGroup = New-AzActionGroup -ResourceGroupName $resourceGroup -Name $actionGroupName -ShortName "alert" `
        -ActionReceiver @(
            @{
                Name = "AlertReceiver"
                EmailAddress = $email
            }
        )
    Write-Host "Action Group erstellt: $actionGroupName"
} else {
    Write-Host "Action Group existiert bereits: $actionGroupName"
}

Write-Host "Monitoring-Setup abgeschlossen! ✅"
