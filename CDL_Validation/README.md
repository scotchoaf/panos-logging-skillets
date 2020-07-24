# Validate Cortex Data Lake Connectivity and Logging

This is a validation skillet to make sure CDL is up and running as expected. It deploys a combination of checking both configurations and 
the systems current connectivity state. As you run the validation skillet and see things that haven't passed, instructions are included in 
the skillet for each test performed on where to get more information and troubleshoot.

### How to use this skillet

This skillet is designed to be used and ran with [Panhandler](http://localhost:8080/panhandler/). You want to import the skillet repository so it shows up in your Skillet Collections under Validation Skillets. Once imported, open and enter firewall information to run the skillet against your 
firewall. 

### Key items

Some key items that this test checks:

* If a CDL connection has been enabled
* If a logging service region has been set 
* If Enhanced Application Logging is enabled on the firewall
* If Traffic Logs are created and forwarded
* If the certificate is verified and not expired
* If a CDL customerID and CDL region are showing up via certificate fetch
* If log forwarding profiles are sending logs to CDL
* If log forwarding profiles have EAL enabled


