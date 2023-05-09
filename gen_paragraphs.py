outp = '{\n'
for t in range(10):
  outp = outp + '"'
  outp = outp + fake.text(32).title()[:-1]
  outp = outp + '":"'
  outp = outp + fake.paragraph(7)
  outp = outp + '",\n'
     
outp = outp[:-2] + "\n}"
print(outp)
