# hello my name is tristi and this is the code for our rotary cell phone which
#shall be managed on a razberry pi zero W

#this brings in the library we need to use the pins on the board
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#set our pins to input or output
GPIO.setup(??, GPIO.OUT)
GPIO.setup(??, GPIO.IN)

#this is the function that each spin of the dial will use to determine what
#that digit will be it is called repedidly if making a outgoing call
def spin ():
    diget=-1
    ca=0
    escape = 0
    pin1 = GPIO.input(1)
    while (pin1=1) and (escape=0):
        while (pin3 == 0):
            pin4 = GPIO.input(4)
            pin3 = GPIO.input(3)
            if (pin4 == 1) and (ca == 0):
                diget= digit + 1
                ca= 1
            elif (pin4 == 0) and (ca==1):
                ca = 0
            else:
                escape=1
    return digit


#start main loop that will allways be running.
#will need to find out how to make sure this program runs on start for the pi
hours_in_day = 24
while hours_in_day == 24:

#scan the input pins and see if we have any values to work with
    pin1 = GPIO.input(1)
    pin2 = GPIO.input(2)
    pin3 = GPIO.input(3)

        #if  there is an incoming call and the phone is on hook then ring
    if (pin1 == 1) and (pin2 == 1):
        while (pin1== 1)and pin2==1):
            pin1 = GPIO.input(1)
            pin2 = GPIO.input(2)
            write pin 6 to 1# wring the phone

            #if while the phone is ringing the phone is picked up then tell the
            #GSM card to connect
        while(pin1 == 0):
            serialport.write()#awnser the phone
            pin1 = GPIO.input(1)

        # if bottom limit switch pressed and phone hung up start dial loop
        #the spin function should be written so that evertying moves from digit
        #to diget and stops and attempts to place the call once the phone is
        #picked up
    if (pin3 == 0) and (pin1 == 0):
        while (pin1 == 0):
            first_diget = spin ()
            second_diget  = spin ()
            second_diget  = spin ()
            third_diget = spin ()
            forth_diget = spin ()
            fifth_diget = spin ()
            sixth_diget = spin ()
            seventh_diget = spin ()
            eight_diget = spin ()
            ninth_diget = spin ()
            tenth_diget = spin ()
            eleventh_diget = spin ()
            twelth_diget = spin ()

        #depending on when the phone was picked up it will send a number with a
        #different amount of digits to the gsm card because area and country codes
        if (twlth diget >= 0):
            phone_number = (first_diget + second_diget + third_diget + forth_diget + fifth_diget + sixth_diget + seventh_diget + eight_diget + ninth_diget + tenth_diget + eleventh_diget + twelth_diget)
        elif (eleventh_diget >= 0):
            phone_number = (first_diget + second_diget + third_diget + forth_diget + fifth_diget + sixth_diget + seventh_diget + eight_diget + ninth_diget + tenth_diget + eleventh_diget)
        elif (tenth_diget >= 0):
            phone_number = (first_diget + second_diget + third_diget + forth_diget + fifth_diget + sixth_diget + seventh_diget + eight_diget + ninth_diget + tenth_diget)
        else:
            phone_number = (first_diget + second_diget + third_diget + forth_diget + fifth_diget + sixth_diget + seventh_diget)

#dial the number and shut the rest of the code up in a loop unitl hang up
        serialport.write("ATD" + phone_number + ';\r')
        while pin1= 0
            pin1 = GPIO.input(1)
