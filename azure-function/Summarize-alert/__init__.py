import logging
import json
import azure.functions as func

# Configure logging
logger = logging.getLogger(__name__)

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function to summarize alerts from Azure Monitor.
    
    Args:
        req: HTTP request containing alert information
        
    Returns:
        HTTP response with summarized alert
    """
    logger.info('Processing alert summarization request')
    
    try:
        # Parse request body
        try:
            req_body = req.get_json()
        except ValueError as e:
            logger.error(f'Invalid JSON in request body: {str(e)}')
            return func.HttpResponse(
                json.dumps({"error": "Invalid JSON in request body"}),
                status_code=400,
                mimetype="application/json"
            )
        
        # Extract alert text
        alert = req_body.get("alert", "")
        
        if not alert:
            logger.warning('No alert text provided in request')
            return func.HttpResponse(
                json.dumps({"error": "No alert text provided"}),
                status_code=400,
                mimetype="application/json"
            )
        
        # Summarize the alert
        summary = summarize_alert(alert)
        logger.info('Alert summarization completed successfully')
        
        return func.HttpResponse(
            json.dumps({"summary": summary}),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logger.error(f'Unexpected error processing alert: {str(e)}', exc_info=True)
        return func.HttpResponse(
            json.dumps({"error": "Internal server error"}),
            status_code=500,
            mimetype="application/json"
        )

def summarize_alert(alert_text: str) -> str:
    """
    Summarize alert text based on content.
    
    Args:
        alert_text: The alert description to summarize
        
    Returns:
        A summarized version of the alert
    """
    if not isinstance(alert_text, str):
        alert_text = str(alert_text)
    
    alert_lower = alert_text.lower()
    
    if "cpu" in alert_lower:
        return "High CPU usage detected. Immediate action recommended."
    elif "disk" in alert_lower:
        return "Low disk space warning. Consider cleanup."
    elif "memory" in alert_lower:
        return "Memory usage alert. Review resource allocation."
    elif "network" in alert_lower:
        return "Network connectivity issue detected. Check network configuration."
    else:
        return "Alert received. Review details for action."
