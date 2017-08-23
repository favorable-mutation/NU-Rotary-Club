# hello my name is tristi and this is the code for our rotary cell phone which
#shall be managed on a razberry pi zero W

#this brings in the library we need to use the pins on the board
#########import RPi.GPIO as GPIO
#########GPIO.setmode(GPIO.BOARD)

#pins that we're using
#########pio = ??????????????????????????
#########pit = ????????????????????????????

#set our pins to input or output
#########GPIO.setup(pio, GPIO.OUT)
#########GPIO.setup(pit, GPIO.IN)

#define the variables used


#this is the function that each spin of the dial will use to determine what
#that digit will be it is called repeatedly if making a outgoing call
def spin ():
    dig = -1
    ca = 0
    esc = 0
    p1spin = input("what is p1 doing")
    if (p1spin == "1") and (esc == 0):
        if (p3spin == "0"):
            p4spin = input("what is p4 doing")
            p3spin = input("what is p3 doing")
            if (p4 == "1") and (ca == 0):
                dig = dig + 1
                ca = 1
            elif (p4 == "0") and (ca == 1):
                ca = 0
            else:
                esc = 1
        else:
            print("foobar")
    else:
        print(dig)


#start main loop that will allways be running.
#will need to find out how to make sure this program runs on start for the pi
    # should be able to use instructions here https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/ ~ Griff
while (input("yes?") == "1"):

    #scan the input pins and see if we have any values to work with
    p1 = input("what is p1 doing")
    p2 = input("what is p2 doing")
    p3 = input("what is p3 doing")

        #if  there is an incoming call and the phone is on hook then ring
    if (p1 == "1") and (p2 == "1"):
        ###while (p1 == 1) and (p2 == 1):
            #p1 = GPIO.input(1)
            #p2 = GPIO.input(2)
            newp1 = input("what is p1 doing now")
            ###############write pin 6 to 1 # ring the phone

            #if while the phone is ringing the phone is picked up then tell the
            #GSM card to connect
            if (newp1 == 0):
            #    serialport.write()#awnser the phone
            #    p1 = GPIO.input(1)
                print("foo")
            else:
                exit()

        # if bottom limit switch pressed and phone hung up start dial loop
        #the spin function should be written so that everything moves from digit
        #to digit and stops and attempts to place the call once the phone is
        #picked up
    if (p3 == "0") and (p1 == "0"):
        #while (p1 == "0"):
        sdig1 = spin ()
        sdig2 = int(input("and"))
        sdig3 = int(input("and"))
        sdig4 = int(input("and"))
        sdig5 = int(input("and"))
        sdig6 = int(input("and"))
        sdig7 = int(input("and"))
        sdig8 = int(input("and"))
        sdig9 = int(input("and"))
        sdig10 = int(input("and"))
        sdig11 = int(input("and"))
        sdig12 = int(input("."))

        #depending on when the phone was picked up it will send a number with a
        #different amount of digits to the gsm card because area and country codes
        if (sdig12 >= 0):
            phone_number = (sdig1, sdig2, sdig3, sdig4, sdig5, sdig6, sdig7, sdig8, sdig9, sdig10, sdig11, sdig12)
        elif (sdig11 >= 0):
            phone_number = (sdig1 + sdig2 + sdig3 + sdig4 + sdig5 + sdig6 + sdig7 + sdig8 + sdig9 + sdig10 + sdig11)
        elif (sdig10 >= 0):
            phone_number = (sdig1 + sdig2 + sdig3 + sdig4 + sdig5 + sdig6 + sdig7 + sdig8 + sdig9 + sdig10)
        else:
            phone_number = (sdig1 + sdig2 + sdig3 + sdig4 + sdig5 + sdig6 + sdig7)

#dial the number and shut the rest of the code up in a loop unitl hang up
        serialport.write("ATD" + phone_number + ';\r')
        while (p1 == 0):
            p1 = GPIO.input(1)

else:
    exit()
