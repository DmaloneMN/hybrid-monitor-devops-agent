"""
Unit tests for the Summarize-alert Azure Function.
"""
import unittest
import json
from unittest.mock import Mock
import azure.functions as func

# Import the function to test
from __init__ import main, summarize_alert


class TestSummarizeAlert(unittest.TestCase):
    """Test cases for the summarize_alert function."""
    
    def test_summarize_cpu_alert(self):
        """Test CPU alert summarization."""
        result = summarize_alert("CPU usage exceeded 90% on VM web-01")
        self.assertEqual(result, "High CPU usage detected. Immediate action recommended.")
    
    def test_summarize_disk_alert(self):
        """Test disk alert summarization."""
        result = summarize_alert("Disk space below 10% on database server")
        self.assertEqual(result, "Low disk space warning. Consider cleanup.")
    
    def test_summarize_memory_alert(self):
        """Test memory alert summarization."""
        result = summarize_alert("Memory usage exceeded 85%")
        self.assertEqual(result, "Memory usage alert. Review resource allocation.")
    
    def test_summarize_network_alert(self):
        """Test network alert summarization."""
        result = summarize_alert("Network connectivity issues detected")
        self.assertEqual(result, "Network connectivity issue detected. Check network configuration.")
    
    def test_summarize_generic_alert(self):
        """Test generic alert summarization."""
        result = summarize_alert("Unknown alert type")
        self.assertEqual(result, "Alert received. Review details for action.")
    
    def test_summarize_case_insensitive(self):
        """Test that alert matching is case-insensitive."""
        result = summarize_alert("HIGH CPU USAGE")
        self.assertEqual(result, "High CPU usage detected. Immediate action recommended.")


class TestMainFunction(unittest.TestCase):
    """Test cases for the main Azure Function endpoint."""
    
    def test_main_with_valid_alert(self):
        """Test main function with valid alert JSON."""
        # Create a mock HTTP request
        req = Mock(spec=func.HttpRequest)
        req.get_json.return_value = {"alert": "CPU usage exceeded 90%"}
        
        # Call the function
        response = main(req)
        
        # Verify response
        self.assertEqual(response.status_code, 200)
        self.assertIn("application/json", response.mimetype)
        response_data = json.loads(response.get_body())
        self.assertIn("summary", response_data)
        self.assertEqual(response_data["summary"], "High CPU usage detected. Immediate action recommended.")
    
    def test_main_with_missing_alert(self):
        """Test main function with missing alert field."""
        req = Mock(spec=func.HttpRequest)
        req.get_json.return_value = {}
        
        response = main(req)
        
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_body())
        self.assertIn("error", response_data)
    
    def test_main_with_invalid_json(self):
        """Test main function with invalid JSON."""
        req = Mock(spec=func.HttpRequest)
        req.get_json.side_effect = ValueError("Invalid JSON")
        
        response = main(req)
        
        self.assertEqual(response.status_code, 400)
        response_data = json.loads(response.get_body())
        self.assertIn("error", response_data)
    
    def test_main_with_exception(self):
        """Test main function handles unexpected exceptions."""
        req = Mock(spec=func.HttpRequest)
        req.get_json.side_effect = Exception("Unexpected error")
        
        response = main(req)
        
        self.assertEqual(response.status_code, 500)
        response_data = json.loads(response.get_body())
        self.assertIn("error", response_data)


if __name__ == '__main__':
    unittest.main()
