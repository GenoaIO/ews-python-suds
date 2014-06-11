# -*- coding: utf-8 -*-
'''
/* EWSWrapper Test & Example usage file
 * ====================================================
 * @author Michal Korzeniowski <mko_san@lafiel.net>
 * @version 0.1
 * @date 10-2011
 * @website http://ewswrapper.lafiel.net/
 * ====================================================
 * Desciption
 * Provides example usage of EWSWrapper
 * To use simple set $to_test to desired action
 * Enumartation of action list in the switch:
 * - calendar_add
 * - calendar_edit
 * - calendar_list
 * - calendar_delete
 * - task_add
 * - task_edit
 * - task_list
 * - task_delete
 * - list_folders
 * 
 * ==================================================*/
'''
import logging
import datetime
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds').setLevel(logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.INFO)
# logging.getLogger('suds.wsdl').setLevel(logging.INFO)


#include EWS wrapper
from ewswrapper.EWSWrapper import EWSDateTime
from ewswrapper.EWSWrapper import EWSWrapper

start_time = datetime.datetime.now()

#user, password & host setup
domain  = 'ExchangeServerName'
user    = 'user.name@domain.com'
pw      = 'Welcome1'

#on_behalf account address
account = 'account.user.name@domain.com'

#base location for wsdl file
datadir = './data'

#create EWSWrapper object
ews = EWSWrapper(host=domain, username=user, password=pw, datadir=datadir,debug=True).wrapper


#what would you like to test tonight?
to_do = 'folder_list'
to_do = 'contacts_list'

if to_do == 'calendar_add':
    items = ews.addCalendarEvent(subject='Test subject', \
                                 body='Test desription', \
                                 start=EWSDateTime(2011, 10, 18, 13, 37, 0), \
                                 end=EWSDateTime(2011, 10, 18, 14, 0, 0), \
                                 attendees=[account], \
                                 on_behalf=account, \
                                 location='Mars')
    print '\nreturned items:'
    for i in items:
        print i
elif to_do == 'calendar_edit':
    items = ews.editCalendarEvent(id='AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYWyAAAYjaWDBdsHQo5pvIdFf3S+AB9cBhZxAAA=', \
                                  ckey='DwAAABYAAAAYjaWDBdsHQo5pvIdFf3S+AB9cCr7N',\
                                  subjcect='New Subject', \
                                  attendees=[account], \
                                  location='Moon')
    print '\nreturned items:'
    for i in items:
        print i   
elif to_do == 'calendar_list':
    items = ews.listCalendarEvent(on_behalf=account, \
                                  start=EWSDateTime(2011, 10, 1, 13, 37, 0), \
                                  end=EWSDateTime(2011, 10, 18, 14, 0, 0), \
                                  shape='DEFAULT_PROPERTIES')
    print '\nreturned items:'
    for i in items:
        print i    
elif to_do == 'calendar_delete':
    items = ews.deleteCalendarEvent(['AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYWyAAAYjaWDBdsHQo5pvIdFf3S+AB9cBhZxAAA='])
    print '\nResults:'
    for i in items:
        print i
        
elif to_do == 'contacts_list':
    items = ews.listContacts(on_behalf=account, \
                                  start=None, \
                                  end=None, \
                                  shape='DEFAULT_PROPERTIES')
    print '\nreturned items:'
    for i in items:
        print "contact_item"  
        print i.CompleteName.FullName
        print i.CompanyName
        if hasattr(i.EmailAddresses.Entry[0],"value"): print "email_1", i.EmailAddresses.Entry[0].value
        if hasattr(i.EmailAddresses.Entry[1],"value"): print "email_2", i.EmailAddresses.Entry[1].value
        if hasattr(i.EmailAddresses.Entry[2],"value"): print "email_3", i.EmailAddresses.Entry[2].value
        print "-"*40        
               
        
if to_do == 'task_add':
    items = ews.addTask(subject='Test Task', \
                        body=u'This is test task', \
                        due=EWSDateTime(2011, 10, 18, 14, 0, 0), \
                        reminderdue=EWSDateTime(2011, 10, 18, 13, 37, 0), \
                        on_behalf='some_email@test.com')
    print '\nreturned items:'
    for i in items:
        print i
if to_do == 'task_edit':
    items = ews.editTask(id='AAMkADkzYjJmNWQ1LTNkYzctNDQxYy05ZTNkLWQ2MjBjOWU2MmU3OABGAAAAAABstM1IOqraQJ32b8x90xBiBwDYjN7FxXrWQpHh4zg87vHzAAAKWdwKAACFWm3OzBDcTYDUBCCa0OxUAAt88oSAAAA=', \
                         ckey='EwAAABYAAACFWm3OzBDcTYDUBCCa0OxUAAt88oyA', \
                         subject=u'Updated Task Subject', \
                         body=u'New body', \
                         due=EWSDateTime(2011, 10, 18, 14, 0, 0), \
                         sensitivity='PERSONAL', \
                         reminderdue=EWSDateTime(2011, 10, 18, 13, 37, 0))
    print '\nreturned items:'
    for i in items:
        print i       
elif to_do == 'task_delete':
    items = ews.deleteTask(['AAMkAGRkNzBkYTNlLTg2NjEtNDA5YS1iOWU3LTY0YWRhZTYzMmUwMgBGAAAAAABVA5BhgjxARYSIPL1mPSAUBwAYjaWDBdsHQo5pvIdFf3S+AAAEQYW3AAAYjaWDBdsHQo5pvIdFf3S+AB9cDCcPAAA='])
    print '\nResults:'
    for i in items:
        print i
elif to_do == 'task_list':
    items = ews.listTask(on_behalf=account, end=EWSDateTime(2011, 10, 18, 13, 37, 0))
    print '\nreturned items:'
    for i in items:
        print i
elif to_do == 'folder_list':
    items = ews.listFolders(on_behalf=account, type='INBOX')
    print '\nreturned items:'
    for i in items:
        print i


end_time = datetime.datetime.now()

print "test completed in: %s" % str(end_time-start_time) 