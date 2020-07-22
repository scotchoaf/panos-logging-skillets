# Cortex Data Lake logging configurations

> This is a beta test branch. please check back in the event this skillet
> is relocated to another repo or branch

The CDL global configuration playbook will configure:

    * global CDL with EAL enabled including the region
    * configuration and system logs using CDL forwarding
    
    
> Designed to run in a python virtual environment
>
> requirements.txt file included in the cdl_playbook_global directory

### running the python script

```angular2
python run_ansible_playbook.py -k {preshared key} -ip {device ip} -u {user} -p {password}
```

The preshared key is found at apps.paloaltonetworks.com in the Cortex Data Lake app.
Part of the firewall onboarding for sw version 9.0.6 or later.

The user credentials are apped to a json dictionary call 'provider' used within
the ansible playbook.

### running the ansible playbook without python

The playbook can be run natively without python or as a skillet.

```angular2
ansible-playbook -i ./inventory.ini cdl.yml
```

> Before running update the preshared key and provider values in vars.yml
> or use the -e extra_vars input. Example syntax in the python file.