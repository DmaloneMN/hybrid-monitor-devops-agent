# Contributing to Hybrid Azure Monitor + DevOps Agent

Thank you for your interest in contributing! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Python version, Azure Functions runtime version)
- Screenshots or logs if applicable

### Suggesting Enhancements

To suggest an enhancement:
- Open an issue with a clear description of the enhancement
- Explain why this enhancement would be useful
- Provide examples of how it would be used

### Pull Requests

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

3. **Test your changes**:
   - Ensure existing tests pass
   - Add new tests for new functionality
   - Test locally using Azure Functions Core Tools

4. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference any related issues

5. **Push to your fork** and submit a pull request to the `main` branch

6. **Wait for review**:
   - Address any feedback from reviewers
   - Make requested changes if needed

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Azure Functions Core Tools
- Azure subscription (for deployment testing)
- Git

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/DmaloneMN/hybrid-monitor-devops-agent.git
   cd hybrid-monitor-devops-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   cd azure-function/Summarize-alert
   pip install -r requirements.txt
   ```

4. Copy the local settings template:
   ```bash
   cp ../local.settings.json.template ../local.settings.json
   # Edit local.settings.json with your configuration
   ```

5. Run the function locally:
   ```bash
   cd ..
   func start
   ```

## Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Use type hints where appropriate

## Testing

- Write tests for new functionality
- Ensure all tests pass before submitting a PR
- Test locally with Azure Functions Core Tools
- Include integration tests where applicable

## Documentation

- Update README.md if you change functionality
- Update relevant documentation in the `docs/` directory
- Add inline comments for complex logic
- Update API documentation if endpoints change

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Questions?

If you have questions about contributing, feel free to open an issue for discussion.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
