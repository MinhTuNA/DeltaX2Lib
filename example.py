import DeltaX2Lib

DeltaX2 = DeltaX2Lib.Deltax2Cmd()
DeltaX2.Home()
DeltaX2.SetAcceleration(1200)
DeltaX2.SetSpeed(200)
for x in range(5):
    DeltaX2.MoveTo(Z=-300)
    DeltaX2.MoveTo(X=0,Y=0)
    DeltaX2.MoveTo(X=-100,Z=-350)
    DeltaX2.MoveTo(Z=-300)
    DeltaX2.MoveTo(X=0,Y=0)
    DeltaX2.MoveTo(X=100,Z=-350)
DeltaX2.Home()
DeltaX2.MoveTo(Z=-350)
DeltaX2.MoveTo(X=50)
DeltaX2.ArcMove(1,X=-50,Y=0,I=-50,J=0)
DeltaX2.ArcMove(0,X=50,Y=0,I=50,J=0)



