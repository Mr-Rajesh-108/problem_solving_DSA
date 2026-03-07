def is_valid(s):
    stack=[]
    mp={')':'(','}':'{',']':'['}
    
    for c in s:
        if c in mp.values():
            stack.append(c)
        else:
            if not stack or stack.pop()!=mp.get(c):
                return "false"
                
    return "true" if not stack else "false"

print(is_valid(input().strip()))