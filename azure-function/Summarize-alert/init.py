import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    alert = req.get_json().get("alert", "")
    summary = summarize_alert(alert)
    return func.HttpResponse(summary, status_code=200)

def summarize_alert(alert_text):
    if "CPU" in alert_text:
        return "High CPU usage detected. Immediate action recommended."
    elif "disk" in alert_text:
        return "Low disk space warning. Consider cleanup."
    else:
        return "Alert received. Review details for action."


function.json
{
  "bindings": [
    {
      "authLevel": "function",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["post"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}


requirements.txt
azure-functions==1.11.0



local.settings.json (excluded from prod)
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}



📁 docs/
architecture-diagram.png
(Placeholder for visual flow: Copilot Studio → Plugin → Azure Function → DevOps)
deployment-checklist.md
# Deployment Checklist

- [x] Provision Azure Function App
- [x] Configure plugin endpoints in Copilot Studio
- [x] Deploy function via GitHub Actions
- [x] Validate alert summarization
- [x] Test pipeline trigger flow


telemetry-setup.md
# Telemetry Setup

## Azure Monitor
- Enable alert rules for CPU, disk, memory
- Route alerts to Log Analytics workspace

## Application Insights
- Instrument Azure Function with App Insights SDK
- Track request rates, failures, and latency



Let me know if you want this scaffold exported as files or zipped for GitHub upload. I can also help you extend this with Purview governance, REST API chaining, or vertical demos. Ready to build!
