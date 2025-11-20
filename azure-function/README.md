# Azure Function - Summarize Alert

This directory contains the Azure Function that summarizes alerts from Azure Monitor.

## Structure

```
azure-function/
├── host.json                          # Function app configuration
├── local.settings.json.template       # Template for local development settings
├── Summarize-alert/
│   ├── __init__.py                    # Main function code
│   ├── function.json                  # Function binding configuration
│   └── requirements.txt               # Python dependencies
└── README.md                          # This file
```

## Local Development

### Prerequisites

- Python 3.9 or higher
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- Azure subscription (for testing with real Azure services)

### Setup

1. Create a local settings file:
   ```bash
   cp local.settings.json.template local.settings.json
   ```

2. Update `local.settings.json` with your configuration values.

3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   cd Summarize-alert
   pip install -r requirements.txt
   cd ..
   ```

5. Start the function locally:
   ```bash
   func start
   ```

The function will be available at `http://localhost:7071/api/Summarize-alert`

## Testing

Test the function using curl:

```bash
curl -X POST http://localhost:7071/api/Summarize-alert \
  -H "Content-Type: application/json" \
  -d '{"alert": "CPU usage exceeded 90% on VM web-01"}'
```

Expected response:
```json
{
  "summary": "High CPU usage detected. Immediate action recommended."
}
```

## Deployment

The function is automatically deployed via GitHub Actions when changes are pushed to the `main` branch. See `.github/workflows/deploy-function.yml` for details.

### Manual Deployment

To deploy manually:

1. Login to Azure:
   ```bash
   az login
   ```

2. Deploy the function:
   ```bash
   func azure functionapp publish <your-function-app-name>
   ```

## Configuration

### Application Settings

The following settings should be configured in Azure Portal or via Azure CLI:

- `APPINSIGHTS_INSTRUMENTATIONKEY`: Application Insights instrumentation key
- `AZURE_OPENAI_ENDPOINT`: (Optional) Azure OpenAI endpoint for advanced summarization
- `AZURE_OPENAI_KEY`: (Optional) Azure OpenAI API key

### Function Authentication

By default, the function uses function-level authentication. The function key is required in the request:

```bash
curl -X POST https://<your-app>.azurewebsites.net/api/Summarize-alert?code=<function-key> \
  -H "Content-Type: application/json" \
  -d '{"alert": "Alert text here"}'
```

For production, consider using Azure AD authentication.

## Error Handling

The function includes comprehensive error handling:

- Returns 400 for invalid JSON or missing alert text
- Returns 500 for unexpected errors
- All errors are logged to Application Insights

## Monitoring

View logs and metrics in:
- Azure Portal > Function App > Monitor
- Application Insights > Logs
- Application Insights > Live Metrics

## Future Enhancements

- Integration with Azure OpenAI for advanced alert summarization
- Support for batch alert processing
- Custom alert classification models
- Integration with Azure AI Foundry models
