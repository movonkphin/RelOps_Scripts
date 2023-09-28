import requests
import csv

# Global Variables
API_URL = "https://api.statuspage.io/v1"
API_KEY = "15fbaf6e-6d84-4e4f-b1ed-172f6ec64fde"
PAGE_ID = None  # This will be initialized when the script runs

def get_component_group_names():
    headers = {"Authorization": f"OAuth {API_KEY}"}

    component_groups_url = f"{API_URL}/pages/{PAGE_ID}/component-groups.json"
    try:
        component_groups_response = requests.get(component_groups_url, headers=headers)
        component_groups_response.raise_for_status()
        component_groups_data = component_groups_response.json()

        return {group["id"]: group["name"] for group in component_groups_data}

    except requests.RequestException as e:
        print(f"Error: {e}")
        return {}

def get_incidents():
    headers = {"Authorization": f"OAuth {API_KEY}"}
    all_incidents = []
    page_num = 1

    while True:
        incidents_url = f"{API_URL}/pages/{PAGE_ID}/incidents.json?page={page_num}&per_page=100"
        try:
            incidents_response = requests.get(incidents_url, headers=headers)
            incidents_response.raise_for_status()
            incidents = incidents_response.json()

            # If no more incidents, break out of the loop
            if not incidents:
                break

            all_incidents.extend(incidents)
            page_num += 1  # Go to the next page

        except requests.RequestException as e:
            print(f"Error: {e}")
            break

    return all_incidents


def main():
    global PAGE_ID

    # Initialize PAGE_ID
    headers = {"Authorization": f"OAuth {API_KEY}"}
    pages_url = f"{API_URL}/pages.json"
    try:
        pages_response = requests.get(pages_url, headers=headers)
        pages_response.raise_for_status()
        pages_data = pages_response.json()
        PAGE_ID = pages_data[0]["id"]  # Assuming only one page, modify if multiple
    except requests.RequestException as e:
        print(f"Error: {e}")
        return

    component_group_names = get_component_group_names()
    incidents = get_incidents()

    # Creating CSV
    with open('incident_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Incident ID', 'Incident Name', 'Impact', 'Status', 'Created At', 'Component Groups', 'Components']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for incident in incidents:
            group_names_for_incident = []

            for component in incident['components']:
                component_group_id = component['group_id']
                group_name = component_group_names.get(component_group_id)
                if group_name and group_name not in group_names_for_incident:
                    group_names_for_incident.append(group_name)

            components_for_incident = [component['name'] for component in incident['components']]

            writer.writerow({
                'Incident ID': incident['id'],
                'Incident Name': incident['name'],
                'Impact': incident['impact'],
                'Status': incident['status'],
                'Created At': incident['created_at'],
                'Component Groups': ', '.join(group_names_for_incident),
                'Components': ', '.join(components_for_incident)
            })

    print("Data has been written to incident_report.csv")

if __name__ == "__main__":
    main()
