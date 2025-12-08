import os
import logging

# Configure logging
log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
log_level = getattr(logging, log_level_str, logging.INFO)
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

def process_data():
    """Simulates a data processing job using environment variables for configuration."""

    logging.info("--- Starting Data Processing Job ---")

    # --- Configuration Variables (read from environment) ---
    data_source_url = os.getenv("DATA_SOURCE_URL")
    api_key = os.getenv("API_KEY")
    output_dir = os.getenv("OUTPUT_DIR", "./processed_data")
    batch_size = int(os.getenv("BATCH_SIZE", "1000"))

    if not data_source_url:
        logging.error("DATA_SOURCE_URL environment variable is not set. Exiting.")
        return
    if not api_key:
        logging.warning("API_KEY environment variable is not set. Proceeding without authentication.")

    logging.info(f"Data Source URL: {data_source_url}")
    logging.info(f"Output Directory: {output_dir}")
    logging.info(f"Batch Size: {batch_size}")
    logging.debug(f"API Key: {'*' * len(api_key) if api_key else '(empty)'}") # Log API key only in debug

    # 1. Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # 2. Simulate fetching data
    logging.info(f"Fetching data from {data_source_url}...")
    # In a real scenario, this would involve network requests, e.g., using 'requests' library
    fetched_data = [f"item_{i}" for i in range(batch_size * 2)] # Simulate some data
    logging.info(f"Fetched {len(fetched_data)} items.")

    # 3. Simulate processing data in batches
    processed_count = 0
    for i in range(0, len(fetched_data), batch_size):
        batch = fetched_data[i:i + batch_size]
        logging.info(f"Processing batch {i // batch_size + 1} with {len(batch)} items...")
        # Simulate some processing logic
        processed_batch = [item.upper() for item in batch]
        
        # Simulate saving processed data
        output_file = os.path.join(output_dir, f"batch_{i // batch_size + 1}.txt")
        with open(output_file, "w") as f:
            for item in processed_batch:
                f.write(item + "\n")
        logging.info(f"Saved processed batch to {output_file}")
        processed_count += len(processed_batch)

    logging.info(f"Total items processed: {processed_count}")
    logging.info("--- Data Processing Job Finished ---")

if __name__ == "__main__":
    process_data()
