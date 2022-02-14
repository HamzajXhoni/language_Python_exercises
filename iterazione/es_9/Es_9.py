while True:
    print("Inserisci un numero")
    N1=int(input())
    print("Inserisci un numero")
    N2=int(input())
    if N2<N1:
        continue
    while N2!=N1-1:
        print(N2)
        N2-=1

