import email.utils
import re
import testcase_study8
pat = r"^[A-Z a-z]{1}[A-Z a-z 0-9 \- \. \, \_]{0,}@[a-z A-Z]{1,}\.[a-z A-Z]{1,3}$"
N = int(input())
for i in range(N):
    nameemail = str(input())
    prs = email.utils.parseaddr(nameemail)
    if bool(re.match(pat,prs[1])):
        print(email.utils.formataddr(prs))