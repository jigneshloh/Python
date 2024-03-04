
import os
# to access windows app
import win32com.client as win32 
olApp = win32.Dispatch("Outlook.Application")
olNS = olApp.GetNameSpace("MAPI")

print(olApp)
mailItem = olApp.CreateItem(0)
mailItem.Subject = 'Job Description'
mailItem.BodyFormat = 1
mailItem.Body = 'Hi Jignesh'
mailItem.To = 'jigneshloh@gmail.com'
mailItem._oleobj_Invoice(*(64209, 0, 8, 0, olNS.Accounts.Item('jigneshloh@gmail.com')))

mailItem.Display()
mailItem.Save()
mailItem.Send()

