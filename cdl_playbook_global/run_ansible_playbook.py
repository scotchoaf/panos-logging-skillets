#!/usr/bin/env python3
# Copyright (c) 2020, Palo Alto Networks
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Authors: Scott Shoaf, Nathan Embery

import click
import json
import subprocess

@click.command()
@click.option("-k", "--cdl_preshared_key", help="onboarding preshared_key", type=str, default='')
@click.option("-ip", "--device_ip", help="device IP address", type=str, default='')
@click.option("-u", "--username", help="API username", type=str, default='admin')
@click.option("-p", "--password", help="API password", type=str, default='Paloalto1')

def cli(cdl_preshared_key, device_ip, username, password):
    """
    run ansible playbook for global Cortex Data Lake configuration
    :param cdl_preshared_key: firewall onboarding PreShared_Key for Cortex Data Lake
    :param device_ip: part of the provider defining device to configure
    :param username: username to access the device
    :param password: password to access the device
    :return: None
    """

    # create a simple provider dict to convert to json and pass as ansible extra-var
    provider_dict = {}
    provider_dict['provider'] = {}
    provider_dict['provider']['ip_address'] = device_ip
    provider_dict['provider']['username'] = username
    provider_dict['provider']['password'] = password
    xvar_provider = json.dumps(provider_dict)

    # ansible command line entry with extra vars
    playbook_cmd = f'ansible-playbook -i inventory.ini cdl.yml'\
                   f' -e cdl_psk={cdl_preshared_key}'\
                   f' -e "{xvar_provider}"'

    # run the playbook and wait until complete
    run_playbook = subprocess.Popen(playbook_cmd, shell=True)
    run_playbook.wait()

if __name__ == '__main__':
    cli()