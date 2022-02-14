while True:
    print("Inserisci un numero")
    N=int(input())
    if N<0:
        continue
    n=N*-1
    while n!=N+1:
        print(n)
        n+=1

