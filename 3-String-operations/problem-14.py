'''
14) Check if an email format is valid in a simple way (must contain one @ and a dot after it).
'''

def meth1(email):

    add_tag_count = 0
    for i, ch in enumerate(email):

        if ch == '@' and add_tag_count >= 1:
            return 'Invalid email'

        if ch == '@':
            add_tag_count += 1

            if i + 1 >= len(email) or email[i+1] == '.' or email[-1] == '.' or '.' not in email[i+1:]:
                return 'Invalid email'

    if add_tag_count == 0:
        return 'Invalid email'

    return 'Valid email'



email = "user@v.com"
print(meth1(email))