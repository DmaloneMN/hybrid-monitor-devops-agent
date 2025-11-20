# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please send an email to the repository owner. All security vulnerabilities will be promptly addressed.

Please include the following information in your report:

- Type of vulnerability
- Full paths of source file(s) related to the manifestation of the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

## Security Best Practices

When using this project:

1. **Secrets Management**: Never commit secrets, API keys, or credentials to the repository. Use Azure Key Vault or GitHub Secrets for sensitive data.

2. **Authentication**: Ensure proper authentication is configured for Azure Functions (function keys, Azure AD authentication).

3. **HTTPS**: Always use HTTPS endpoints for production deployments.

4. **Dependencies**: Regularly update dependencies to patch known vulnerabilities. Run `pip list --outdated` to check for updates.

5. **Access Control**: Use Azure RBAC (Role-Based Access Control) to limit access to Azure resources.

6. **Monitoring**: Enable Application Insights and Azure Monitor to detect suspicious activities.

7. **Input Validation**: The Azure Function includes input validation, but always verify data at each layer.

## Known Security Considerations

- **Azure Function Authentication**: The default configuration uses function-level authentication. For production, consider using Azure AD authentication.
- **API Keys**: Store all API keys and secrets in Azure Key Vault, not in configuration files.
- **Network Security**: Consider using Virtual Network integration for Azure Functions in production.
