def binario():
    global x
    bin = list()
    while(x>=1):
        bin.append(int(x%2))
        x = x/2
    print(bin[::-1])
resp = "S"
while(resp=="S" or resp=="s"):
    x = int(input("Digite um número decimal:"))
    binario()
    resp = input("Deseja continuar? S/N:\n")
    while(resp!="S" and resp!="s" and resp!="N" and resp!="n"):
        resp = input("Digite apenas S ou N!\n")
