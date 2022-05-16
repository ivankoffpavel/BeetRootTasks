for a in range (1, 20):
  i = 2
  if a == 1:
     print(f"{a} is not a start-simple number")
  else:
    while i < a:
        if a % i == 0:
            print (f"{a} is not a simple number")
            break
        else:
            i += 1
    else:
        print(f"{a} is a simple number")