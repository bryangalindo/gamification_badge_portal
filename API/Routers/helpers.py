from Data.connection import Table


def get_badge_requests_list(application_id: str):
    requests = Table('requests')
    requests_data = requests.query("ApplicationID", application_id)
    return requests_data.items


def add_badge_requests_to_applications(applications: list):
    updated_applications = []
    for app in applications:
        app_id = app['RowKey']
        badge_requests_list = get_badge_requests_list(app_id)
        app['requests'] = badge_requests_list
        updated_applications.append(app)
        
    return updated_applications

def add_badge_request_to_requests_table(badges: list):
    requests_table = Table('requests')
    for badge in badges:
        requests_table.insert(badge)
        
def delete_badge_requests_from_requests_table(application_id: str):
    requests_table = Table('requests')
    requests_data = requests_table.query("ApplicationID", application_id)
    for badge in requests_data.items:
        requests_table.delete(partition_key=badge.PartitionKey, row_key=badge.RowKey)
