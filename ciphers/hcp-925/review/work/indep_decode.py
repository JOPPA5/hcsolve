# Independent reviewer decode of hcp-925 from the reviewer's own row-by-row reading of work/hires pic (crops in review/work)
rows = """25.20.12.7.5.2.20.19.18.19.1.7.5
1.11.18.9.3.8.8.5.20.19.5.6.17.20.8.5.17.20.8.5.17.22.1.3
8.19.5
20.13.4.1.13.12.5.9.13.5.13.11.9.5.2.11.9.13.7.4.1.3.8.19.5
6.9.5.11.12.9.17.4.5.17.7.5.4.1.13.10.5.5.9.13
8.5.20.19.12.20.18.18.5.9.13.7.5.2.20.19.18.19.1.7.18.5.9.13
18.5.13.4.5.19
4.5.9.13
11.9.5.2.11.9.13.7
10.1.19.3.8.5.13.8.14.19.19.20.12""".split()
alpha = [chr(c) for c in range(65, 91) if chr(c) != 'J']
n = 0; used = set(); s = ''
for r in rows:
    g = list(map(int, r.split('.'))); n += len(g); used |= set(g)
    s += ''.join(alpha[x-1] for x in g); print(''.join(alpha[x-1] for x in g))
print('groups', n, 'distinct', sorted(used))
