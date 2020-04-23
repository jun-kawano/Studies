import email.utils
n = int(input())
raw_emails = []
for i in range(n):
    raw_emails.append(input())

valid_emails = []

def user_check(user1):
    if re.search(r"^[^A-Za-z][^0-9\w\.-]*", user1):
        return False
    return True

for item in raw_emails:
    name, email_addr = email.utils.parseaddr(item)

    if "@" in email_addr and "." in email_addr:

        i1 = email_addr.index("@")

        dom_ext = email_addr[i1+1 :]

        i2 = (dom_ext.index(".") + i1 + 1)

        user = email_addr[ : i1]
        domain = email_addr[i1+1 : i2]
        ext = email_addr[i2+1 : ]

        #print(f"u  {user}|, d  {domain}|, e  {ext}|, i1 = {i1}|, i2 = {i2}")

        if user_check(user):
            if domain.isalpha():
                if ext.isalpha():
                    if 0 < len(ext) < 4:
                        valid_emails.append((name, email_addr))

#print(f"valid  {valid_emails}")

for item in valid_emails:
    print(email.utils.formataddr(item))
