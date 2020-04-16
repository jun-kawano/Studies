

import email.utils
n = int(input())
raw_emails = []
for i in range(n):
    raw_emails.append(input())

valid_emails = []

for item in raw_emails:
    name, email_addr = email.utils.parseaddr(item)
    i1 = email_addr.index("@")
    i2 = email_addr.index(".")

    user = email_addr[ : i1]
    domain = email_addr[i1+1 : i2]
    ext = email_addr[i2+1 : ]

    if user[0].isalpha() and user[1:].isalnum() and domain.isalpha() and ext.isalpha():
        valid_emails.append((name, email_addr))

#print(type(valid_emails[0]))
#print(valid_emails)

for item in valid_emails:
    #user, address = item
    #print(item)
    #print(email.utils.formataddr(user, address))
    print(email.utils.formataddr(item))


#print(type(email.utils.parseaddr(raw_emails[0])))