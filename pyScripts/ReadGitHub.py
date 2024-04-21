from urllib.request import urlopen, Request        # Importing urllib library

import json                                        # Importing JSON
import ssl                                         # Importing SSL
import requests

# GitHub repo details
REPO_OWNER = "dip06ece"
REPO_NAME = "OPSRoom"
REPO_BRANCH = "main"

# Jenkins job details
JENKINS_SERVER = "http://localhost:8100"
TARGET_JOB = "OPSRoom_GitHub_ProofMain"
TARGET_JOB_BUILD_TOKEN = "OPSRoom_ProofMain"
JENKINS_USER = "admin"
AUTHENTICATION_TOKEN = "1162ff19ad303356ef2ccd5e71f748f401"


class ReadGitHub:                                  # Define a class
    def fetch_openPullRequests(self):
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
            if (item["base"]["ref"] ==REPO_BRANCH):      # If the base branch is $REPO_BRANCH only
                all_pull_request.append(item["id"])     # Append pull id to list
            all_pull_request.append(item["base"]["sha"])     # Append pull id to list

        return all_pull_request                     # Return the pull_id list



myRepoReadObj = ReadGitHub()                        # Creating object
open_pull_requests = myRepoReadObj.fetch_openPullRequests() # Reading pull list
for item in open_pull_requests:                     # For each item in list
    target_project_url = JENKINS_SERVER + "/job/"+TARGET_JOB+"/buildWithParameters/"
                                                    # Construct Target project URL
    params = {                                      # Project Parameters
        "token": TARGET_JOB_BUILD_TOKEN,
        "PullRequestNumber": item
    }

    auth = (JENKINS_USER, AUTHENTICATION_TOKEN)     # Define the authentication credentials
    response = requests.post(target_project_url, params=params, auth=auth)
                                                    # Sending a POST request to JENKINS
    # Check the response status
    if response.status_code == 201:
        print("Build triggered successfully!")
    else:
        print("Failed to trigger the build. Status code:", response.status_code)
        print("Response:", response.text)





