import requests

# The link should be of the file directly
url = 'https://youtube.com/clip/UgkxPFMxp4bRPA7pgO2nS7GQ8UtiYR_loQqE'
file_extension = '.wav'   # Example .wav
r = requests.get(url)

# If extension does not exist in end of url, append it
if file_extension not in url.split("/")[-1]:
        filename = f'{url[31:40]}{file_extension}'
# Else take the last part of the url as filename
else:
        filename = url.split("/")[-1]

with open(filename, 'wb') as f:
        # You will get the file in base64 as content
        f.write(r.content)