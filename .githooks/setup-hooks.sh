#!/bin/bash

# Setup script to configure git hooks

echo "🔧 Setting up git hooks..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Configure git to use the .githooks directory
git config core.hooksPath .githooks

# Make the hooks executable
chmod +x .githooks/pre-commit
chmod +x .githooks/pre-push

echo "✓ Git hooks configured successfully!"
echo ""
echo "The following hooks are now active:"
echo "  - pre-commit: Runs before each commit"
echo "  - pre-push: Runs before each push"
echo ""
echo "They will check for:"
echo "  - Linting errors (flake8)"
echo "  - Code formatting (black)"
echo "  - Import sorting (isort)"
echo "  - Debugger statements"
echo ""
echo "Install linting tools with:"
echo "  pip install flake8 black isort"

