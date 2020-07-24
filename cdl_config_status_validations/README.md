# Validate Cortex Data Lake Connectivity and Logging

This is a validation skillet to make sure CDL is up and running as expected. It deploys a combination of checking both configurations and 
the systems current connectivity state. As you run the validation skillet and see things that haven't passed, instructions are included within 
the skillet file for each test performed and where to get more information for each test.

### How to use this skillet

This skillet is designed to be played with [panHandler](https://live.paloaltonetworks.com/t5/skillet-tools/install-and-get-started-with-panhandler/ta-p/307916)
and requires API connectivity between panHandler and the NGFW in order to capture
system state information not found in the configuration files.

When playing the skillet in panHandler select `Online` mode.

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


