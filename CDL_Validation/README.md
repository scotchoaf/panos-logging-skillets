#Validate CDL connectivity and Logging


### CDL enabled Test

* Check if CDL is enabled for log forwarding capabilities
* if CDL not connected go to [Connect Firewalls to Cortex Data Lake](https://docs.paloaltonetworks.com/cortex/cortex-data-lake/cortex-data-lake-getting-started/get-started-with-cortex-data-lake/key.html)

### Logging Service Regions Test

* Check if a logging service region has been set on the Firewall UI
* If Region has not been set or is unavailable, need to on-board firewall and License to CDL

### Enhanced Application Logging for firewall Test

* Check if EAL is enabled on you firewall to collect data and incerease visibility
* EAL must be enabled for device to push logs to CDL
* If EAL is not enabled troubleshoot via [Enhanced Application Logging](https://docs.paloaltonetworks.com/pan-os/8-1/pan-os-new-features/management-features/enhanced-application-logging.html)

### Check Logging Status

* Want to check two things here, if traffic logs are created and if they are forwarded
* Logging status is good if these values are not Null and do not equal "Not Available"

### Certificate Verification for CDL

Command used
> request logging-service-forwarding certificate info

Block to ensure CDL certification is validated

* Make sure certificate chain is set to "OK"
* Make sure public and private keys match
* Make sure certificate has not expired

### Customer Region and ID verification

Command used
> request logging-service-forwarding customerinfo show

Block to ensure CDLregion and CDLCustomerID has been generated and is showing up

* Tests if CDL region and CDL customerID is set
* If either test fails, check that certificate fetch was successful

### Sending logs to CDL enabled test

Block to verify if all profiles have sending to CDL enabled

* Captures a list of profiles that have sending to CDL enabled
* Captures a list of every profile within the firewall, sending to CDL or not
* Compares list to determine which profiles aren't sending to CDL
* Display which profiles that don't have sending to CDL enabled
* Can configure profiles for CDL via Objects -> Log Forwarding on firewall

### Enhanced Application Logging on profiles enabled test

Block to verify if all profiles have EAL enabled

* Captures a list of profiles that have EAL enabled
* Captures a list of every profile within the firewall, EAL enabled or not
* Compares list to determine which profiles aren't sending to CDL
* Display which profiles that don't have sending to CDL enabled
* Can configure profiles for EAL via Objects -> Log Forwarding on firewall
