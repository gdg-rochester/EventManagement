import requests


def get_attendees(start_index, end_index):
    url = 'https://www.explara.com/api/e/attendee-list'
    data = {'eventId': 'EBEHBIFF', 'fromRecord': start_index, 'toRecord': end_index}
    headers = {
        'Authorization': 'Bearer 7a294cd04ca570bfb7c1dc763bf7a0c5f328d8b9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.post(url, data=data, headers=headers)
    response = response.json()
    return response
