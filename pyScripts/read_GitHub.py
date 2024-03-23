from urllib.request import urlopen, Request  # Importing urllib library


import json                                  # Importing JSON
import ssl                                   # Importing SSL

REPO_OWNER = "dip06ece"
REPO_NAME = "OPSRoom"
REPO_BRANCH = "main"
class ReadGitHub:                                  # Define a class
    def fetch_open_pull_requests(self):
        # Building URL
        URL = "https://api.github.com/repos/"+REPO_OWNER+"/"+REPO_NAME+"/pulls"

        ssl_context = ssl.create_default_context()  # Set SSL context
        ssl_context.check_hostname = False          # Hostname Verification off
        ssl_context.verify_mode = ssl.CERT_NONE     # Certificate verification off

        request = Request(URL)                      # Create request for URL
        response = urlopen(request,context=ssl_context)
                                                    # Request with custom SSL context

        data_json = json.loads(response.read())     # Load data in JSON

        all_pull_request = []                       # Taking an empty list
        for item in data_json:                      # For every item in Json Data
            all_pull_request.append(item["id"])     # Append pull id to list

        return all_pull_request                     # Return the pull_id list

myRepoReadObj = ReadGitHub()                    # Creating object
open_pull_requests = myRepoReadObj.fetch_open_pull_requests() # Reading pull list
for item in open_pull_requests:                 # For each item in list
    print(item)
