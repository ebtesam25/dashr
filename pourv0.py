import Adeept
import time
import pyttsx3


milk = 100.0
tea = 100.0
coffee = 100.0
water = 100.0
sugar = 100.0


def pispeak(sentence):
    eng = pyttsx3.init()
    eng.setProperty('rate', 130) 
    eng.say(sentence)
    eng.runAndWait()
    print(sentence)
    eng.stop()


com_port = 'COM3'

Apos = 90
Bpos = 90
Cpos = 90
Dpos = 90
Epos = 60


def resetpos():
    moveArm(148, 90, 180, 80, 60)
    time.sleep(1)
    moveForce2(148, 90, 180, 80, 60)



def readypos():
    moveArm(90, 90, 90, 80, 60)
    time.sleep(1)
    #moveForce2(90, 90, 90, 80, 60)


def drinkpos1():
    moveArm(148, 24, 104, 80, 60)
    time.sleep(1)
    moveForce2(148, 24, 104, 80, 60)


def drinkpos2():
    moveArm(148, 24, 104, 80, 30)
    time.sleep(1)
    



def drinkpos3():
    moveArm(148, 24, 104, 80, 60)
    time.sleep(1)



def drinkpos4():
    moveArm(56, 90, 180, 80, 50)
    time.sleep(1)



def drinkpos5():
    moveArm(156, 90, 180, 180, 50)
    time.sleep(1)



def drinkpos6():
    moveArm(180, 90, 180, 180, 50)
    time.sleep(1)



def drinkpos7():
    moveArm(180, 90, 180, 180, 0)
    time.sleep(1)


def servpos1():
    moveArm(156, 47, 130, 80, 55)
    time.sleep(1)
    
def servpos2():
    moveArm(156, 47, 130, 80, 35)
    time.sleep(1)
    

    
# base D1 148
# shoulder D2 90
# elbow D3 180 (edited) 
# 4:52
# Wrist D4 80
# Finger D5 60


def serial_connect(com):    #Call this function to connect with the server
    # global ADDR,tcpClicSock,BUFSIZ,ip_stu,ipaddr,ser
    # com=E1.get()       #Get the IP address from Entry
    Adeept.com_init(com,115200,1)
    Adeept.wiat_connect()
    Adeept.three_function("'servo_attach'",0,9)
    Adeept.three_function("'servo_attach'",1,6)
    Adeept.three_function("'servo_attach'",2,5)
    Adeept.three_function("'servo_attach'",3,3)
    Adeept.three_function("'servo_attach'",4,11)
    # E1.config(state='disabled')   #Disable the Entry
    # Btn14.config(state='disabled')   #Disable the Entry
    
    print(com+':Succesfully connected ARM ')
    



def moveArm(A, B, C, D, E):
    
    speed = 0.01
    global Apos, Bpos, Cpos, Dpos, Epos
    
    
    if Apos >= A:
        for i in range(Apos,A,-1):
            Adeept.three_function("'servo_write'",0,str(i))
            time.sleep(speed)
    
    
    if Apos < A:
        for i in range(Apos,A):
            Adeept.three_function("'servo_write'",0,str(i))
            time.sleep(speed)
            
    Apos = A   
    
    # Adeept.three_function("'servo_write'",0,A)
    # time.sleep(1)
    

    if Bpos >= B:
        for i in range(Bpos,B,-1):
            Adeept.three_function("'servo_write'",1,str(i))
            time.sleep(speed)
    
    if Bpos < B:
        for i in range(Bpos,B):
            Adeept.three_function("'servo_write'",1,str(i))
            time.sleep(speed)

    Bpos = B
    
    if Cpos >= C:
        for i in range(Cpos,C,-1):
            Adeept.three_function("'servo_write'",2,str(i))
            time.sleep(speed)
    
    if Cpos < C:
        for i in range(Cpos,C):
            Adeept.three_function("'servo_write'",2,str(i))
            time.sleep(speed)

    Cpos = C    

    if Dpos >= D:
        for i in range(Dpos,D,-1):
            Adeept.three_function("'servo_write'",3,str(i))
            time.sleep(speed)
    
    if Dpos < D:
        for i in range(Dpos,D):
            Adeept.three_function("'servo_write'",3,str(i))
            time.sleep(speed)

    Dpos = D

    if Epos >= E:
        for i in range(Epos,E,-1):
            Adeept.three_function("'servo_write'",4,str(i))
            time.sleep(speed)
    
    if Epos < E:
        for i in range(Epos,E):
            Adeept.three_function("'servo_write'",4,str(i))
            time.sleep(speed)

    Epos = E

    
    # Adeept.three_function("'servo_write'",1,B)
    # time.sleep(1)
    # Adeept.three_function("'servo_write'",2,C)
    # time.sleep(1)
    # Adeept.three_function("'servo_write'",3,D)
    # time.sleep(1)
    # Adeept.three_function("'servo_write'",4,E)


def moveForce():
    
    global Apos, Bpos, Cpos, Dpos, Epos
    Adeept.three_function("'servo_write'",0,Apos)
    time.sleep(1)
    Adeept.three_function("'servo_write'",1,Bpos)
    time.sleep(1)
    Adeept.three_function("'servo_write'",2,Cpos)
    time.sleep(1)
    Adeept.three_function("'servo_write'",3,Dpos)
    time.sleep(1)
    Adeept.three_function("'servo_write'",4,Epos)


def moveForce2(A, B, C, D, E):
    
    # global Apos, Bpos, Cpos, Dpos, Epos
    Adeept.three_function("'servo_write'",0,A)
    time.sleep(1)
    Adeept.three_function("'servo_write'",1,B)
    time.sleep(1)
    Adeept.three_function("'servo_write'",2,C)
    time.sleep(1)
    Adeept.three_function("'servo_write'",3,D)
    time.sleep(1)
    Adeept.three_function("'servo_write'",4,E)


def scale(x,y,w):
    global var_A,var_B, var_C,var_D,var_E
    def pix_send1(event):
        time.sleep(0.03)
        Adeept.three_function("'servo_write'",0,var_A.get())
        #print(var_A.get())
    def pix_send2(event):
        time.sleep(0.03)
        Adeept.three_function("'servo_write'",1,var_B.get())
        #print(var_B.get())
    def pix_send3(event):
        time.sleep(0.03)
        Adeept.three_function("'servo_write'",2,var_C.get())
        #print(var_C.get())
    def pix_send4(event):
        time.sleep(0.03)
        Adeept.three_function("'servo_write'",3,var_D.get())
        #print(var_D.get())
    def pix_send5(event):
        time.sleep(0.03)
        Adeept.three_function("'servo_write'",4,var_E.get())
        #print(var_E.get())


##test

# serial_connect(com_port)

# readypos()

# drinkpos1()
# drinkpos2()
# drinkpos3()
# drinkpos4()
# drinkpos5()
# drinkpos6()
# drinkpos7()
# servpos1()
# servpos2()
# servpos1()

# readypos()



def testpour(dname):
    global milk, sugar, coffee, tea, water
    global com_port
    serial_connect(com_port)
    print("start -- now doing readypos")
    moveArm(90, 90, 90, 80, 60)
    time.sleep(1)

    # jack

    moveArm(90, 90, 90, 80, 30)
    time.sleep(1)

    print("-- now doing drinkpos2")
    moveArm(148, 24, 104, 80, 30)
    time.sleep(1)

    print("-- now doing drinkpos3")
    moveArm(148, 24, 104, 80, 60)
    time.sleep(1)

    moveArm(148, 90, 180, 80, 60)
    time.sleep(1)

    moveArm(90, 90, 180, 80, 60)
    time.sleep(1)

    print("-- now doing lower")
    moveArm(90, 24, 90, 80, 60)
    time.sleep(1)

    moveArm(90, 24, 90, 148, 60)
    time.sleep(1)

    moveArm(90, 24, 90, 80, 60)
    time.sleep(1)


    # put back

    print("-- now doing drinkpos2")
    moveArm(148, 24, 104, 80, 60)
    time.sleep(1)

    print("-- now doing drinkpos3")
    moveArm(148, 24, 104, 80, 30)
    time.sleep(1)

    # coke 

    # jack

    moveArm(90, 90, 90, 80, 30)
    time.sleep(1)

    print("-- now doing drinkpos2")
    moveArm(10, 24, 104, 80, 30)
    time.sleep(1)

    print("-- now doing drinkpos3")
    moveArm(10, 24, 104, 80, 60)
    time.sleep(1)

    moveArm(10, 90, 180, 80, 60)
    time.sleep(1)

    moveArm(90, 90, 180, 80, 60)
    time.sleep(1)

    print("-- now doing lower")
    moveArm(90, 24, 90, 80, 60)
    time.sleep(1)

    moveArm(90, 24, 90, 148, 60)
    time.sleep(1)

    moveArm(90, 24, 90, 80, 60)
    time.sleep(1)


    # put back

    print("-- now doing drinkpos2")
    moveArm(10, 24, 104, 80, 60)
    time.sleep(1)

    print("-- now doing drinkpos3")
    moveArm(10, 24, 104, 80, 30)
    time.sleep(1)


    # done

    moveArm(90, 90, 70, 80, 30)
    time.sleep(0.1)

    moveArm(90, 90, 120, 80, 30)
    time.sleep(0.1)

    moveArm(90, 90, 60, 80, 30)
    time.sleep(0.1)

    moveArm(90, 90, 120, 80, 30)
    time.sleep(0.1)

    moveArm(90, 90, 60, 80, 30)
    time.sleep(0.1)

    moveArm(90, 90, 120, 80, 30)
    time.sleep(0.2)

    moveArm(90, 90, 60, 80, 30)
    time.sleep(0.2)

    # complete

    moveArm(90, 90, 104, 80, 60)
    time.sleep(0.2)
    
    
    dname = dname.lower()
    
    pispeak("hey human, here's your " + dname + ", ingredient levels updated. Thanks for using dashArm.")

    if dname == 'latte' :
        milk = milk - 10.0
        coffee = coffee - 10.0
        sugar = sugar - 5.0
        water = water - 15.0
    
    if dname == 'cappuccino' :
        milk = milk - 5.0
        coffee = coffee - 15.0
        sugar = sugar - 5.0
        water = water - 15.0
    
    if dname == 'chai' :
        milk = milk - 10.0
        tea = tea - 10.0
        sugar = sugar - 5.0
        water = water - 15.0
    
    if dname == 'mocha' :
        milk = milk - 10.0
        coffee = coffee - 15.0
        sugar = sugar - 5.0
        water = water - 10.0
        
    
    ings = {}

    
    if milk <=20.0:
        ings['milk'] =  'low'
    else:        
        ings['milk'] = 'normal'

    if sugar <=20.0:
        ings['sugar'] =  'low'
    else:        
        ings['sugar'] = 'normal'

    if water <=20.0:
        ings['water'] =  'low'
    else:        
        ings['water'] = 'normal'

    if tea <=20.0:
        ings['tea'] =  'low'
    else:        
        ings['tea'] = 'normal'

    if coffee <=20.0:
        ings['coffee'] =  'low'
    else:        
        ings['coffee'] = 'normal'
        
    # ings['sugar'] = 'normal'
    # ings['coffee'] = 'normal'
    # ings['tea'] = 'normal'
    # ings['water'] = 'normal'

    print (ings)
    
    return ings
    

def resetlevels():
    global tea, coffee, water, sugar, milk
    tea = 100.0
    coffee = 100.0
    water = 100.0
    sugar = 100.0
    milk = 100.0


# 
# testpour("latte")
