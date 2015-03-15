# ssh_connection.py
# Byers Applied Python example with mistakes or additions by Phil

import paramiko
import time

class SSHConnection(object):
    
#   Using base ssh class to support Cisco
#   and subclasses for other vendors
    
#   We want to
#   - initialize with a network device object
#   - obtain ssh credentials
#   - establish our connection
#   - pass commands to eliminate LF and unwanted prompts
#   - eventually enable and config
    
    def __init__(self, net_device):
        self.net_device = net_device
        self.ip = net_device.ip_address
        
        # We have passed in the device and saved local attributes
        
        if net_device.ssh_port:
            self.port = net_device.ssh_port
        else:
            self.port = 22
            
        self.username = net_device.credentials.username
        self.password = net_device.credentials.password
        
    def establish_connection(self):
        
        print
        print "." * 80
        
        # Use paramiko to create local sshclient object
        
        self.remote_conn_pre = paramiko.SSHClient()
        
        # Allow untrusted hosts to be added automically
        
        self.remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Initiate SSH connection and map login parameters to paramiko
        
        print "SSH connecton established to {}:{}".format(self.ip, self.port)       
    
        self.remote_conn_pre.connect(hostname=self.ip, port=self.port, username=self.username, password=self.password)
        
        
        # Use invoke_shell to establish interactive session
        
        self.remote_conn = self.remote_conn_pre.invoke_shell()
        print "Interactice SSH session establishe..."
        
        
        # Strip initial router prompt
        time.sleep(3)     # Added for Arista because prompt did not arrive quickly
        output = self.remote_conn.recv(1000)
        
        
        # View output
        print output
        print "."*80
        print
        
        
        
