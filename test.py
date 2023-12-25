import requests
from datetime import datetime, timedelta

def test_register_doctor():
    url = 'http://10.50.2.238:8012/doctors/register'
    data = {
        'name': 'John Doe',
        'specialty': 'Gyneco',
        'city': 'Wavre',
        'email': 'johndoe@example.com',  # Ensure this email is unique and not already registered
        'phone_number': '2128146903',
        'hospital_name': 'Clinique Saint Lambert',
        'password': 'test123'  # Provide a new password for registration
    }

    response = requests.post(url, json=data)
    print(response.json())

def test_login_doctor(): 
    url = 'http://10.50.2.238:8012/doctors/login'
    data = {
        'email': 'janesmith@example.com',  # Use the email address you registered the doctor with
        'password': 'test123'  # Use the password you set for the doctor
    }

    response = requests.post(url, json=data)
    print(response.json())

def test_get_doctor():
    doctor_id = 6
    # Replace '1' with the actual DoctorID you want to retrieve
    public_info_url = f'http://10.50.2.238:8012/doctors/{doctor_id}'

    # Send a GET request
    response = requests.get(public_info_url)

    # Print out the response
    print(response.json())

def test_update_doctor():
    # First, log in to get the token
    login_url = 'http://10.50.2.238:8012/doctors/login'
    login_data = {
        'email': 'janesmith@example.com',
        'password': 'test123'
    }
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json().get('token')

    doctor_id = 6

    update_data = {
        'name': 'Jane Smith Updated',
        'specialty': 'Pediatrics',
        'city': 'New Springfield',
        # You can add other fields to update as needed
    }
    
    # Then, attempt to update the doctor's profile
    update_url = f'http://10.50.2.238:8012/doctors/{doctor_id}'
    headers = {'x-access-tokens': token}
    
    response = requests.put(update_url, headers=headers, json=update_data)
    print(response.json())


def test_update_delay():
    # Log in to get the token
    login_url = 'http://10.50.2.238:8012/doctors/login'
    login_data = {
        'email': 'janesmith@example.com',
        'password': 'test123'
    }
    login_response = requests.post(login_url, json=login_data)
    token = login_response.json().get('token')

    doctor_id = 6
    new_delay_duration = 0
    
    # Update the delay
    update_url = f'http://10.50.2.238:8012/delays/{doctor_id}'
    headers = {'x-access-tokens': token}
    update_data = {
        'delay_duration': new_delay_duration,
        'start_timestamp': datetime.utcnow().isoformat() + 'Z',  # Convert to ISO 8601 format
        'end_timestamp': (datetime.utcnow() + timedelta(minutes=120)).isoformat() + 'Z',  # Convert to ISO 8601 format
        'announcement_timestamp': datetime.utcnow().isoformat() + 'Z'  # Convert to ISO 8601 format
    }
    
    response = requests.put(update_url, headers=headers, json=update_data)
    print(response.json())


def test_get_current_delay():
    doctor_id = 6
    url = f'http://10.50.2.238:8012/delays/{doctor_id}'

    # Send a GET request to the endpoint
    response = requests.get(url)

    # Print out the response
    print(response.json())


def test_search_doctors():
    url = 'http://10.50.2.238:8012/doctors'
    params = {
        'name': '',
        'city': 'Sydney',
        'specialty': ''
    }

    response = requests.get(url, params=params)
    print(response.json())

def test_get_all_doctors():
    url = 'http://10.50.2.238:8012/doctors/all'

    response = requests.get(url)
    print(response.json())

test_get_all_doctors()

