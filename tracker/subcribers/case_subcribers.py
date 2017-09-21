# Module handles users subcrible case


# Sms helper

from __future__ import print_function # python 2/3 compatibility for example code

import telerivet
   
API_KEY = 'ZHGQzNYLWmpcwBs1yS6QtEImhbOGZ1h8'  # from https://telerivet.com/api/keys
PROJECT_ID = 'PJ4dcc6197b9642c25'

tr = telerivet.API(API_KEY)

project = tr.initProjectById(PROJECT_ID)

# Send a SMS message
project.sendMessage(
    to_number = '+23277032015',
    content = 'Hello world!'
)

# Query contacts  
name_prefix = 'Alan';
cursor = project.queryContacts(
    name = {'prefix': name_prefix},
    sort = 'name'    
).limit(20)

print("%d contacts matching %s:\n" % (cursor.count(), name_prefix))

for contact in cursor:
    print(contact.name, contact.phone_number, contact.vars.birthdate)

# Import a contact
contact = project.getOrCreateContact(
    name = 'John Smith',
    phone_number = '555-0001',
    vars = {
        'birthdate': '1981-03-04',
        'network': 'Vodacom'
    }
)

# Add a contact to a group    
group = project.getOrCreateGroup('Subscribers')
contact.addToGroup(group)