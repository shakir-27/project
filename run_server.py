import os
import sys

def run_server():
    """Simulates a web server startup using environment variables for configuration."""

    # --- Configuration Variables (read from environment) ---
    # Server settings
    server_port = int(os.getenv("SERVER_PORT", "8000"))
    debug_mode = os.getenv("DEBUG_MODE", "False").lower() == "true"

    # Database settings
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = int(os.getenv("DB_PORT", "5432"))
    db_user = os.getenv("DB_USER", "admin")
    db_password = os.getenv("DB_PASSWORD", "password")
    db_name = os.getenv("DB_NAME", "app_database")

    print("--- Starting Web Server ---")
    print(f"Server Port: {server_port}")
    print(f"Debug Mode: {debug_mode}")
    print("\n--- Database Configuration ---")
    print(f"DB Host: {db_host}")
    print(f"DB Port: {db_port}")
    print(f"DB User: {db_user}")
    print(f"DB Name: {db_name}")
    print(f"DB Password: {'*' * len(db_password) if db_password else '(empty)'}") # Mask password

    # Simulate server startup logic
    if debug_mode:
        print("\nRunning in DEBUG mode. Extra logging enabled.")
    else:
        print("\nRunning in PRODUCTION mode.")

    # In a real application, you would initialize your web framework here
    # e.g., app.run(host='0.0.0.0', port=server_port, debug=debug_mode)
    print("\nWeb server initialized successfully (simulated).")
    print("--- Server Ready ---")

if __name__ == "__main__":
    run_server()
