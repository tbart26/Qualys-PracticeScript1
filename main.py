# Qualys Platform: US3; https://qualysguard.qg3.apps.qualys.com
# API URLSs for Asset Inventory, EDR, File Integrity Monitoring, and CS:
# API - https://qualysapi.qg3.apps.qualys.com
# Gateway - https://gateway.qg3.apps.qualys.com
# Cloud Agent Servers: https://qagpublic.qg3.apps.qualys.com
# Container Security Servers: https://cmsqagpublic.qg3.apps.qualys.com/ContainerSensor
# API Endpoint: Noted by the documentation - depends on function being used

import qualysapi

# This is out API URL for Host Assets
connect = qualysapi.connect(remember_me=True)
api_url = "/api/2.0/fo/asset/host/"

##############################################################################################################
# Essentially, these are the list of parameters we want to call for when shooting the request over to the API.
# We want tags, basic details, and for one specific IP
##############################################################################################################

params = {

    'action': 'list', # Almost mandatory. Haven't found a reason to not include it.
    'details': 'Basic/AGs', # Read docs for options. Lets you decide how verbose you want info to be.
    'show_tags': 1, # We only really have the option between 0 and 1. This lets us enable/disable tags if we like.
    'ips': '<IP/IP Range>', # Self-explanatory. Replace <> values with your IP/IP range.

}

##########################################
# Now we actually perform the API request.
##########################################

resp = connect.request(api_url, params)
print(resp)  # This will output the response, or at least it should.
