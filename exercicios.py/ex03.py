#eh_par(n°), retornar True p par e False p impar

def eh_par(x):
    if (x%2)==0:
        return True
    else:
        return False
    
while True:
    n= int(input("dgt um nmr: "))
    if eh_par(n):
        print("True")
    else:
        print("False")