#!/bin/bash

# This script simulates a deployment process using environment variables.

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration Variables (read from environment) ---
APP_NAME=${APP_NAME:-"my-web-app"}
DEPLOY_ENV=${DEPLOY_ENV:-"development"}
GIT_REPO_URL=${GIT_REPO_URL:-"https://github.com/user/my-web-app.git"}
DEPLOY_PATH=${DEPLOY_PATH:-"/var/www/$APP_NAME"}
VIRTUALENV_PATH=${VIRTUALENV_PATH:-"/opt/venvs/$APP_NAME"}

echo "--- Starting Deployment for $APP_NAME in $DEPLOY_ENV environment ---"
echo "Repository: $GIT_REPO_URL"
echo "Deployment Path: $DEPLOY_PATH"

# 1. Create deployment directory if it doesn't exist
if [ ! -d "$DEPLOY_PATH" ]; then
    echo "Creating deployment directory: $DEPLOY_PATH"
    sudo mkdir -p "$DEPLOY_PATH"
    sudo chown -R $USER:$USER "$DEPLOY_PATH"
fi

# 2. Clone or pull the repository
echo "Cloning/Pulling repository..."
if [ -d "$DEPLOY_PATH/.git" ]; then
    echo "Repository already exists. Pulling latest changes..."
    git -C "$DEPLOY_PATH" pull origin main
else
    echo "Cloning repository into $DEPLOY_PATH..."
    git clone "$GIT_REPO_URL" "$DEPLOY_PATH"
fi

# 3. Set up Python virtual environment (if applicable)
echo "Setting up virtual environment..."
if [ ! -d "$VIRTUALENV_PATH" ]; then
    echo "Creating virtual environment at $VIRTUALENV_PATH"
    python3 -m venv "$VIRTUALENV_PATH"
fi
source "$VIRTUALENV_PATH/bin/activate"

# 4. Install dependencies
echo "Installing Python dependencies..."
pip install -r "$DEPLOY_PATH/requirements.txt"

# 5. Run database migrations (example)
if [ "$DEPLOY_ENV" == "production" ]; then
    echo "Running database migrations..."
    python "$DEPLOY_PATH/manage.py" migrate
fi

# 6. Collect static files (example)
echo "Collecting static files..."
python "$DEPLOY_PATH/manage.py" collectstatic --noinput

# 7. Restart application service (example - replace with actual service management)
echo "Restarting application service (simulated)..."
echo "Service for $APP_NAME in $DEPLOY_ENV restarted successfully."

echo "--- Deployment Complete ---"
