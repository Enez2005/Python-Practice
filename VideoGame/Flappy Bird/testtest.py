import time

run = True
VEL = 0

def gravity(VEL):
    return VEL + 1



while run == True:
    time.sleep(0.1)
    
    VEL = gravity(VEL)

    print(VEL)
