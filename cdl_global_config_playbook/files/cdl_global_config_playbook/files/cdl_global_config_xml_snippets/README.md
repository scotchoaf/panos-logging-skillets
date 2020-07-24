# Cortex Data Lake XML Snippets

This skillet has a small set of XML snippets to configure the global elements of CDL
in the NGFW:

    * CDL enabled, Enhanced Application Logging (EAL) enabled
    * CDL region configured
    * System and Configuration logs configured for CDL log forwarding
    
This skillet does not configure log fowarding profiles or add profiles
to security policies.

> This XML skillet is used by the Ansible playbook to provide coverage
> for configuration elements not covered in the panos Ansible collection.

