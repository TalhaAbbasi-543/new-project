n = int(input("Please Enter Number Is it Factor or not : -"))
count = 0
for i in range(1,n+1):
   if n % i == 0:
      count += 1
      print (count)
   else: 
      print("it is not Perfect Nmuber ")