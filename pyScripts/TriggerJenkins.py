import jenkins                              # Importing Jenkins (Installed by pip)
import time                                 # Importing time

# Jenkins Authentication URL
JENKINS_URL = "http://localhost:8100"
JENKINS_USERNAME = "admin"
JENKINS_PASSWORD = "admin"

class DevOpsJenkins:
    def __init__(self):                             # Try to connect to Jenkins Server with provided uid and pwd
        try:
            self.jenkins_server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)
            user = self.jenkins_server.get_whoami()
            version = self.jenkins_server.get_version()
            print ("Jenkins Version: {}".format(version))
            print ("Jenkins User: {}".format(user['id']))
        except jenkins.JenkinsException as e:
            print("Error: Failed to connect to Jenkins server. Reason:", str(e))

    def build_job(self, name, parameters=None, token=None):
        try:
            next_build_number = self.jenkins_server.get_job_info(name)['nextBuildNumber']
            self.jenkins_server.build_job(name, parameters=parameters, token=token)
            while True:
                build_info = self.jenkins_server.get_build_info(name, next_build_number)
                if build_info['building']:
                    time.sleep(5)  # Poll every 5 seconds
                else:
                    break
            return build_info
        except jenkins.JenkinsException as e:
            print("Error: Failed to trigger build for job '{}'. Reason:".format(name), str(e))

if __name__ == "__main__":
    NAME_OF_JOB = "OPSRoom_GitHub_ProofMain"
TOKEN_NAME = "OPSRoom_ProofMain"
PARAMETERS = {'project': 'devops'}  # Example Parameter
jenkins_obj = DevOpsJenkins()
if jenkins_obj:
    output = jenkins_obj.build_job(NAME_OF_JOB, PARAMETERS, TOKEN_NAME)
    if output:
        print("Jenkins Build URL:", output['url'])