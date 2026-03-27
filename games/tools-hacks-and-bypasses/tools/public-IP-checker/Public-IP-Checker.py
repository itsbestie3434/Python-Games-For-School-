import requests

def get_public_ip():
    # Fetches the machine's public IP address using an external API.
    try:
        response = requests.get('https://api.ipify.org')
        # Raise an exception for bad status codes
        response.raise_for_status() 
        ip_data = response.json()
        return ip_data['ip']
    except requests.exceptions.RequestException as e:
        return f"Error fetching public IP: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    print(f"Your Public IP Address is: {public_ip}")
  print("Made By ItsBestie3434, Thanks for using my tool!")
