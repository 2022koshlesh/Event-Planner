@echo off
REM Setup script to configure git hooks for Windows

echo Setting up git hooks...

REM Configure git to use the .githooks directory
git config core.hooksPath .githooks

echo Git hooks configured successfully!
echo.
echo The following hooks are now active:
echo   - pre-commit: Runs before each commit
echo   - pre-push: Runs before each push
echo.
echo They will check for:
echo   - Linting errors (flake8)
echo   - Code formatting (black)
echo   - Import sorting (isort)
echo   - Debugger statements
echo.
echo Install linting tools with:
echo   pip install flake8 black isort

pause

