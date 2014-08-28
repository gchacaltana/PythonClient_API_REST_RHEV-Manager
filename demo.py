# -*- coding: utf-8 -*-
 
__author__      = "Gonzalo Chacaltana @gchacaltanab"
 
from rhevmanager import RhevManager
 
class Demo(object):
    def __init__(self,api_url,username,password,cert):
        self.api_url = api_url
        rhev_username = username
        rhev_password = password
        rhev_cert = cert
        self.rhevm = RhevManager(self.api_url,rhev_username,rhev_password,rhev_cert)
        self.endpoints = self.build_link_resource_rhevm()
 
    def build_link_resource_rhevm(self):
        """Crea lista de recursos del home document del API REST"""
        data = self.rhevm.get_home_document()
        endpoints =  {}
        for item in data['link']:
            endpoints[item['rel']] = self.api_url + item['href']
        return endpoints
 
    def get_templates(self, template_id=None):
 
        url_format = self.endpoints['templates']
        url = url_format + "/" + template_id if template_id != None else url_format
        return self.rhevm.request(url)
 
    def get_events(self, event_id = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['events']
        url = url_format + "/" + event_id if event_id != None else url_format
        return self.rhevm.request(url)
 
    def get_users(self, user_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['users']
        url = url_format + "/" + user_guid if user_guid != None else url_format
        return self.rhevm.request(url)
 
    def get_vm(self, vm_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['vms']
        url = url_format + "/" + vm_guid if vm_guid != None else url_format
        return self.rhevm.request(url)
 
     def get_clusters(self, cluster_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['clusters']
        url = url_format + "/" + cluster_guid if cluster_guid != None else url_format
        return rhevm.request(url)
 
    def get_datacenters(self, datacenter_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['datacenters']
        url = url_format + "/" + datacenter_guid if datacenter_guid != None else url_format
        return rhevm.request(url)
 
    def get_hosts(self, host_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['hosts']
        url = url_format + "/" + host_guid if host_guid != None else url_format
        return rhevm.request(url)
 
    def get_networks(self, network_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['networks']
        url = url_format + "/" + network_guid if network_guid != None else url_format
        return rhevm.request(url)
 
    def get_roles(self, role_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['roles']
        url = url_format + "/" + role_guid if role_guid != None else url_format
        return rhevm.request(url)
 
    def get_storagedomains(self, storagedomain_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['storagedomains']
        url = url_format + "/" + storagedomain_guid if storagedomain_guid != None else url_format
        return rhevm.request(url)
 
    def get_tags(self, tag_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['tags']
        url = url_format + "/" + tag_guid if tag_guid != None else url_format
        return rhevm.request(url)
 
    def get_groups(self, group_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['groups']
        url = url_format + "/" + group_guid if group_guid != None else url_format
        return rhevm.request(url)
 
    def get_domains(self, domain_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['domains']
        url = url_format + "/" + domain_guid if domain_guid != None else url_format
        return rhevm.request(url)
 
    def get_vmpools(self, vmpool_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['vmpools']
        url = url_format + "/" + vmpool_guid if vmpool_guid != None else url_format
        return rhevm.request(url)
 
    def get_disks(self, disk_guid = None):
 
        rhevm = self.connect_rhev_manager()
        url_format = self.endpoints['disks']
        url = url_format + "/" + disk_guid if disk_guid != None else url_format
        return rhevm.request(url)
 
 
obj = Demo(api_url,username,password,cert)
obj.get_events()
obj.get_users()
obj.get_templates()
obj.get_clusters()
obj.get_datacenters()
obj.get_hosts()
obj.get_networks()
