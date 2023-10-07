#3 towers, 4 discs, larger disc should never be on top of the smaller disc
def printMove(fr,to):
    print('move from '+str(fr)+' to '+str(to))
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
Towers(4,1,2,3)