- intent: getActiveAlerts
  tool: azure-monitor
  inputs:
    subscriptionId: "{{user.subscriptionId}}"
    api-version: "2019-05-05"
    Authorization: "Bearer {{tools.azure-token-fetcher.access_token}}"