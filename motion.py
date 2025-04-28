from decimal import Decimal
import math
from enum import Enum

class Constant(Enum):
    G = Decimal(6.6743 * math.pow(10,-11))
    M_e = Decimal(5.9722 * math.pow(10,24))
    R_e = Decimal(6.371 * math.pow(10,6))

class Motion():
    def velocity_Y(g: Decimal, time: int) -> Decimal:
        return Decimal((Decimal(g)*(math.pow(time,2))/2))
    
    def position_X():
        ...

    def position_Y(height: int, g: Decimal, time: int):
        return height + Decimal(Decimal(g) * (time**2) /2)

    def acceleration_of_free_fall(G: Decimal, M: Decimal, R: Decimal) -> Decimal:
        return Decimal(G*M)/Decimal(R**2);