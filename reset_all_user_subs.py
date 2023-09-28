import requests
import json
import time

API_ENDPOINT = 'https://api.statuspage.io/v1'  # Replace with the base URL of the statuspage API
API_KEY = '15fbaf6e-6d84-4e4f-b1ed-172f6ec64fde'  # Replace with your API key
PAGE_ID = '2vs6q4d52kq2' # Replace with your page ID
SUBSCRIBERS_PER_PAGE = 100

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def get_all_subscribers():
    """
    Fetch all subscribers for a given page with pagination.
    """
    subscribers = []
    page_num = 1

    while True:
        response = requests.get(f"{API_ENDPOINT}/pages/{PAGE_ID}/subscribers?page={page_num}", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if not data:  # No more subscribers
                break
            subscribers.extend(data)
            page_num += 1
            time.sleep(1.1)  # Respect rate limit for next page fetch
        else:
            print(f"Error {response.status_code}: Could not fetch subscribers for page {page_num}")
            break

    return subscribers

def update_subscriber(subscriber_id):
    """
    Update a subscriber to subscribe to all components by excluding the component_ids parameter.
    """
    data = {}
    response = requests.patch(f"{API_ENDPOINT}/pages/{PAGE_ID}/subscribers/{subscriber_id}", headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        print(f"Successfully updated subscriber {subscriber_id}.")
    else:
        print(f"Error {response.status_code}: Failed to update subscriber {subscriber_id}. Reason: {response.text}")

def main():
    subscribers = get_all_subscribers()

    if not subscribers:
        print("No subscribers fetched. Exiting.")
        return

    print(f"Found {len(subscribers)} subscribers. Starting updates...")

    for subscriber in subscribers:
        update_subscriber(subscriber['id'])
        time.sleep(1.1)  # Introducing a delay to respect the API rate limit

    print("All subscribers updated successfully.")

if __name__ == '__main__':
    main()
