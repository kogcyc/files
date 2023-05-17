from sys import argv
from subprocess import check_output as cout

a = argv[1]
b = list(a)
c = ''
for t in list(b):
	c = c + f'grep -v {t} | '
d = argv[2]
e = ''
for t in list(d):
	e = e + f'grep {t} | '
f = 'cat s5.txt | ' + c + e
if len(argv) > 3:
	for t in range(len(argv)-3):
		u = t + 3
		f = f + f'grep "{argv[u]}" | '  
#f = f + 'grep "....[^]..." | '
#f = f + 'grep "....[^]..." '

output = cout(f[:-2], shell=True)
print(output.decode('ascii'))

#print(f[:-2])