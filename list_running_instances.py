#!/bin/python

import sys
#import s3_key
import boto.s3.connection
from pprint import pprint
from boto import ec2
import boto.ec2

AWS_ACCESS_KEY_ID="<CUT>"
AWS_SECRET_ACCESS_KEY="<CUT>"
# definition of region we want to get
region_name='eu-west-1'

# definition of which instances we want to grab
tag_name=sys.argv[1]
print tag_name

# creating hook to ansible hosts file, and writing the basename
target = open('hosts_' + tag_name, 'w')

#ec2conn = ec2.connection.EC2Connection(s3_key.AWS_ACCESS_KEY_ID, s3_key.AWS_SECRET_ACCESS_KEY, region = ec2.get_region(region_name))
ec2conn = boto.ec2.connect_to_region("eu-west-1", aws_access_key_id="<CUT>", aws_secret_access_key="<CUT>")
#ec2conn = ec2.connection.EC2Connection(s3_key.AWS_ACCESS_KEY_ID, s3_key.AWS_SECRET_ACCESS_KEY, region = ec2.get_region(region_name))

# filter based by name passed by command line arguments - like prod* or devprod*
reservations = ec2conn.get_all_instances(filters={'tag:Name': tag_name, 'instance-state-name': 'running'})

#getting instances
all_addresses = ec2conn.get_all_addresses()

instances = [ i for r in reservations for i in r.instances]
for i in instances:
        ip_address = getattr(i, 'ip_address')
        print ip_address
        target.write(ip_address)
        target.write("\n")
        #pprint(i.__dict__)
