#User function Template for python3

from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                graph[email].append(account[1])
                graph[account[1]].append(email)
                email_to_name[email] = name

        def dfs(email, connected_emails):
            if email not in visited:
                visited.add(email)
                connected_emails.append(email)
                for neighbor in graph[email]:
                    dfs(neighbor, connected_emails)

        merged_accounts = []
        visited = set()
        for email in graph:
            if email not in visited:
                connected_emails = []
                dfs(email, connected_emails)
                merged_accounts.append([email_to_name[email]] + sorted(connected_emails))

        return merged_accounts

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends
