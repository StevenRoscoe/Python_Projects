import yaml
import requests
import time
import signal
import sys

# Global variable to store endpoint results
endpoint_results = {}

def parse_config_file(file_path):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data

def health_check(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', ''),
        )
        if 200 <= response.status_code < 300 and response.elapsed.total_seconds() < 0.5:
            return "UP"
        else:
            return "DOWN"
    except requests.exceptions.RequestException as e:
        return "DOWN"

def log_results():
    for domain, results in endpoint_results.items():
        total_tests = len(results)
        up_count = sum(1 for result in results if result == "UP")
        availability_percentage = (up_count / total_tests) * 100
        print(f"{domain} has {int(availability_percentage)}% availability percentage")

def signal_handler(sig, frame):
    print("\nProgram exited. Logging final results:")
    log_results()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) != 2:
        print("Usage: python script.py <config_file_path>")
        sys.exit(1)

    config_file_path = sys.argv[1]
    config_data = parse_config_file(config_file_path)

    try:
        while True:
            # Health checks for each endpoint
            for endpoint in config_data:
                endpoint_name = endpoint.get('name', 'Unknown')  # Provide a default value
                result = health_check(endpoint)

                if endpoint_name not in endpoint_results:
                    endpoint_results[endpoint_name] = []

                endpoint_results[endpoint_name].append(result)

            # Log results after each testing cycle
            log_results()

            # Wait for 15 seconds before the next cycle
            time.sleep(15)

    except KeyboardInterrupt:
        # Handle user exit (CTRL+C)
        print("\nProgram exited. Logging final results:")
        log_results()