# Cortex Data Lake Set Commands 

### Prerequisites

* Need versions 9.0.6 or higher for everything to run smoothly
* Need to generate PSK via [the Hub](https://apps.paloaltonetworks.com/apps)
* Once at the hub go into Cortex Data Lake -> Firewall On-Boarding -> Generate PSK
* Need to select a region to set the logging service forwarding towards
* This is done via activating the CDL app in the hub

### Fetch Logging License

*  Fetch licenses for firewall 
*  Check license info for verification 
*  Check valid customerinfo and ID displayed

### Establish and Check CDL Connection

* Use the pre-shared key as the vcariable to certify CDL connection with firewall
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

