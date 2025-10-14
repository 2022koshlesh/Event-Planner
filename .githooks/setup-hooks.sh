#!/bin/bash

# Setup script to configure git hooks

echo "🔧 Setting up git hooks..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Configure git to use the .githooks directory
git config core.hooksPath .githooks

# Make the pre-commit hook executable
chmod +x .githooks/pre-commit

echo "✓ Git hooks configured successfully!"
echo ""
echo "The pre-commit hook will now run automatically before each commit."
echo "It will check for:"
echo "  - Linting errors (flake8)"
echo "  - Code formatting (black)"
echo "  - Import sorting (isort)"
echo "  - Debugger statements"
echo ""
echo "Install linting tools with:"
echo "  pip install flake8 black isort"

