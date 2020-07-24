# PAN-OS Logging Skillets

Suite of skillets and playbooks to simplify configuration of Cortex Data Lake (CDL).

Summary information is provided below with more details capture in each skillet directory.

Skillets can be played using 
[panHandler](https://live.paloaltonetworks.com/t5/skillet-tools/install-and-get-started-with-panhandler/ta-p/307916)
 by importing this repository. The Ansible playbook can be played natively in Ansible,
 by using the python script, or in panHandler.
 

### Prerequisites

The following are required to activate and configure CDL for a PAN-OS NGFW:

   * minimum software version 9.0.6
   * activated logging-service subscription
   * generate and copy onboarding preshared key via [the Hub](https://apps.paloaltonetworks.com/apps)
   * have the region associated to CDL in the app at [the Hub](https://apps.paloaltonetworks.com/apps)


### After CDL is globally enabled

The global configuration playbook and skillets create a baseline with a working implementation
of CDL. The validation skillets can be used to validate the NGFW system status.

Additonal configuration is then required to create CDL/EAL enabled log forwarding profiles
or update existing log forwarding profiles. The last step is to ensure these profiles
are being used within security policies to capture and forwarding logs such as traffic
and threat.
    
### CDL Set Commands

Output set commands to screen to copy-paste into the CLI.

A combination of operation and configure commands to update licenses,
fetch the CDL service certicate, enable CDL with enhanced application logging,
and configure CDL logging for configuration and system logs.

### CDL Ansible Playbook

This playbook is designed to enable CDL with Enhanced Application Logging and
configure system and configuration log forwarding. Once the playbook completes,
the NGFW will have CDL globally enabled.

### CDL XML Skillet

This skillet uses the NGFW API to quickly configure CDL with EAL with the NGFW
after the CDL service has been activated.

The Ansible playbook references this skillet as part of the configuration process
for XML elements not currently supported in the panos collection.

### Add CDL and EAL to log forwarding profiles

Allows the user to enter a profile name and update existing log type rules with
CDL while also enabling and adding log entries for EAL logs.

