from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import re

import requests

from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = False

        result = super(ActionModule, self).run(tmp, task_vars)

        result["guest_info"] = {
            "env": {},
            "vnc": {},
            "ipv4": None,
            "ipv6": None,
            "moid": "vm-63",
            "tags": [],
            "vimref": "vim.VirtualMachine:vm-63",
            "hw_eth0": {
              "label": "ethernet-0",
              "summary": "DVSwitch: fea97929-4b2d-5972-b146-930c6d0b4014",
              "macaddress": "00:0c:29:36:63:62",
              "addresstype": "generated",
              "ipaddresses": [],
              "portgroup_key": "dvportgroup-13",
              "macaddress_dash": "00-0c-29-36-63-62",
              "portgroup_portkey": None
            },
            "hw_name": "DC0_H0_VM0",
            "hw_files": [
              "[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.vmx",
              "[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.nvram",
              "[LocalDS_0] DC0_H0_VM0/vmware.log",
              "[LocalDS_0] DC0_H0_VM0/disk1.vmdk"
            ],
            "identity": {},
            "tpm_info": {
              "provider_id": None,
              "tpm_present": None
            },
            "hw_folder": "DC0/vm",
            "module_hw": True,
            "snapshots": [],
            "annotation": None,
            "hw_cluster": None,
            "hw_version": "vmx-13",
            "hw_guest_id": "otherGuest",
            "customvalues": {},
            "hw_esxi_host": "DC0_H0",
            "hw_datastores": [
              "LocalDS_0"
            ],
            "hw_interfaces": [
              "eth0"
            ],
            "instance_uuid": "b4689bed-97f0-5bcd-8a4c-07477cc8f06f",
            "guest_question": None,
            "hw_is_template": False,
            "hw_memtotal_mb": 32,
            "hw_power_status": "poweredOn",
            "hw_product_uuid": "265104de-1472-547c-b873-6dc7883fb6cb",
            "current_snapshot": None,
            "advanced_settings": {
              "govcsim": "TRUE"
            },
            "hw_guest_ha_state": None,
            "guest_tools_status": "guestToolsNotRunning",
            "hw_guest_full_name": None,
            "hw_processor_count": 1,
            "guest_tools_version": "0",
            "hw_cores_per_socket": 1,
            "guest_consolidation_needed": False
          },
          {
            "env": {},
            "vnc": {},
            "ipv4": None,
            "ipv6": None,
            "moid": "vm-63",
            "tags": [],
            "vimref": "vim.VirtualMachine:vm-63",
            "hw_eth0": {
              "label": "ethernet-0",
              "summary": "DVSwitch: fea97929-4b2d-5972-b146-930c6d0b4014",
              "macaddress": "00:0c:29:36:63:62",
              "addresstype": "generated",
              "ipaddresses": [],
              "portgroup_key": "dvportgroup-13",
              "macaddress_dash": "00-0c-29-36-63-62",
              "portgroup_portkey": None
            },
            "hw_name": "DC0_H0_VM0",
            "hw_files": [
              "[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.vmx",
              "[LocalDS_0] DC0_H0_VM0/DC0_H0_VM0.nvram",
              "[LocalDS_0] DC0_H0_VM0/vmware.log",
              "[LocalDS_0] DC0_H0_VM0/disk1.vmdk"
            ],
            "identity": {},
            "tpm_info": {
              "provider_id": None,
              "tpm_present": None
            },
            "hw_folder": "DC0/vm",
            "module_hw": True,
            "snapshots": [],
            "annotation": None,
            "hw_cluster": None,
            "hw_version": "vmx-13",
            "hw_guest_id": "otherGuest",
            "customvalues": {},
            "hw_esxi_host": "DC0_H0",
            "hw_datastores": [
              "LocalDS_0"
            ],
            "hw_interfaces": [
              "eth0"
            ],
            "instance_uuid": "a4689bed-97f0-5bcd-8a4c-07477cc8f06f",
            "guest_question": None,
            "hw_is_template": False,
            "hw_memtotal_mb": 32,
            "hw_power_status": "poweredOn",
            "hw_product_uuid": "265104de-1472-547c-b873-6dc7883fb6cb",
            "current_snapshot": None,
            "advanced_settings": {
              "govcsim": "TRUE"
            },
            "hw_guest_ha_state": None,
            "guest_tools_status": "guestToolsNotRunning",
            "hw_guest_full_name": None,
            "hw_processor_count": 1,
            "guest_tools_version": "0",
            "hw_cores_per_socket": 1,
            "guest_consolidation_needed": False
        }

        #result['msg'] = 'This is my message, maybe it is structured?'
        #result['my_children'] = {
        #    'child_1': {
        #        'changed': True,
        #    },
        #    'child_2': {
        #        'changed': False,
        #    },
        #    'child_3': {
        #        'grandchildren': {
        #            'grandchild_1': {
        #                'changed': True,
        #            }
        #        }
        #    }
        #}
        result['changed'] = False
        return result