with open('basics.py') as f:
  print(f.read(3))
  print('-----------------')
  print(f.readline())


f2 = open('basics.py')
print(f2.read(10))
# good pratice to close file after open
f2.close()