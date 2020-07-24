# Cortex Data Lake Set Commands 

This skillet contains configuration operation commands(set commands) to configure and securely connect your firewall to CDL. Also validates that everything is running smoothly will also be checked along the way. the pieces needed to successfully get CDL up and running

### Prerequisites

* Need versions 9.0.6 or higher for everything to run smoothly
* Need to generate PSK via [the Hub](https://apps.paloaltonetworks.com/apps)
* Once at the hub go into Cortex Data Lake -> Firewall On-Boarding -> Generate PSK
* Need to select a region to set the logging service forwarding towards
* This is done via activating the CDL app in the hub

### Key Items

Key Items included in the skillet are:

* Fetching the license for verification
* On-boarding using pre-shared key 
* Checking that we have the key
* Perform global configurations for CDL that enables enhanced application logging

### How to use this Skillet

This Skillet is designed to be used and ran with [Panhandler](http://localhost:8080/panhandler/). However you may also opt to
perform a manual text swap of the two variables within the Skillet which are "preshared_key" and "cdl_region". The preshared_key
variable is found via accessing the hub and going into Cortex Data Lake to Firewall On-Boarding and generating a PSK, this is your
preshared_key. The cdl_region is the host region you selected when activating your Cortex Data Lake application.


### Fetch Logging License

*  Fetch licenses for firewall 
*  Check license info for verification 
*  Check valid customerinfo and ID displayed

### Establish and Check CDL Connection

* Use the pre-shared key as the variable to certify CDL connection with firewall
* Checks jobs status to ensure certificate fetch successful should show FIN - OK
* Check that logging-service-forwarding certificate is verified and not expired

### Configure Firewall for CDL using set Commands

* Enter configure mode on firewall
* Enable logging service forwarding
* Set logging service forwarding region using region variable from pre-requisite
* Enable enhanced application logging for increased visibility into network activity
* Disable log suppression so similar logs don't combine
* Set config log forwarding filter to "All logs" to forward every log
* Set config log forwarding to send everything to CDL
* Set system log forwarding filter to "All logs" to forward every log
* Set system log forwarding to send everything to CDL
* Commit changes to firewall
* Exit out of configure mode

### Check CDL Status

* Check to see if "'Log Collection log forwarding agent' is active and connected"

