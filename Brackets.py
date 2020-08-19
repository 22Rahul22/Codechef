def m(s):
    bal = 0
    m_bal = 0
    for i in range(len(s)):
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1
        m_bal = max(m_bal, bal)
    return m_bal


t = int(input())
for _ in range(t):
    a = input()
    x = m(a)
    b = ""
    for i in range(x*2):
        if i < x:
            b += '('
        else:
            b += ')'
    print(b)