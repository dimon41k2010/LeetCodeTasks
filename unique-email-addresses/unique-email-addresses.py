class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            edit_email = edit_local_name(local_name) + "@" + domain_name
            res.add(edit_email)

        return (len(res))


def edit_local_name(s):
    if '+' in s:
        s = s.split("+")[0]
    res_list = []
    for char in s:
        if char != ".":
            res_list.append(char)
    return ''.join(res_list)        
        
        
#Time: O(N * E)  This is still linear complexity
#Space: O(N * E)
