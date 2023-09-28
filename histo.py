import requests
import matplotlib.pyplot as plt

# Replace these with your actual API key and page ID
BASE_URL = "https://api.statuspage.io/v1"
API_KEY = "15fbaf6e-6d84-4e4f-b1ed-172f6ec64fde"
PAGE_ID = "2vs6q4d52kq2"

# Set the headers with your API key
HEADERS = {
    "Authorization": f"OAuth {API_KEY}",
    "Content-Type": "application/json"
}

def get_histogram_data():
    """
    Get the histogram data from the Statuspage API.
    """
    url = f"{BASE_URL}/pages/{PAGE_ID}/subscribers/histogram_by_state"
    
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    
    return response.json()

def plot_histogram(data):
    """
    Plot the histogram based on the provided data.
    """
    subscriber_types = list(data.keys())
    total_counts = [data[subscriber_type]['total'] for subscriber_type in subscriber_types]
    
    plt.bar(subscriber_types, total_counts)
    plt.xlabel('Subscriber Type')
    plt.ylabel('Total Count')
    plt.title('Subscribers Histogram by Type')
    plt.xticks(rotation=45)  # Rotate X-axis labels for better readability
    plt.tight_layout()       # Adjust layout to ensure everything fits properly
    plt.show()

def main():
    histogram_data = get_histogram_data()
    plot_histogram(histogram_data)

if __name__ == "__main__":
    main()
