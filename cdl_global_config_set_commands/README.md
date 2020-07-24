# Cortex Data Lake Set Commands 

This skillet contains CLI configuration and operation commands to configure and securely connect your firewall to CDL. 
Also includes are operation commands to validate system status during setup.

> This skillet does not leverage API access to the firewall and instead requires
> the user to copy-paste commands using CLI access

### Prerequisites

In addition to the base prerequisites:

* CLI access to the firewall

### How to use this Skillet

#### With panHandler

This skillet can be run in panHandler by inputting the preshared key and region
values. The output is text information on the screen that can be captured, shared,
or copy-pasted directly into the CLI.

#### Without panHandler

Users can manually edit the cdl_cli_commands.conf text file substituting the variables
found as {{ variables }} within the file.

### Key Items

Key Items included in this skillet are:

* Fetching the license for verification
* On-boarding using pre-shared key 
* Checking that we have the key
* Perform global configurations for CDL that enables enhanced application logging

