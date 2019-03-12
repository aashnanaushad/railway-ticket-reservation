import pickle
import os
import random

def pass_details():                 
        name=str(raw_input("\n\nEnter passenger name:"))
        fstat=str(raw_input("\nJourney from station:"))
        tstat=str(raw_input("\nTo:"))
        doj=raw_input("\nEnter DATE of Journey:")
        gender=str(raw_input("\nM/F :"))
        tno=int(raw_input("\ntrain number:"))
                                                
        a=("pnr"+name)
     
        f=open(a+".dat","w")                            
        print ">>>>>>>>>>>>>>TICKET RESERVED <<<<<<<<<<<<<<<<<"
        c=random.randint(10000,99999)
        print "your pnr no is",c
        f.write(name)
        f.write('\n')
        f.write(fstat)
        f.write('\n')
        f.write(tstat)
        f.write('\n')
        f.write(doj)
        f.write('\n')
        f.write(gender)
        f.write('\n')
        f.close()
def cancel():
        zx=str(raw_input("Name of the passenger:"))
        zz=int(raw_input("PNR number:"))
        os.remove('C:\Python27\pnr'+zx+'.dat')
def display_passdetails():
        z=str(raw_input("ENTER YOUR NAME : "))
        X=int(raw_input("ENTER PNR number :"))
        ra=random.randint(1,99)
        f2=open(r'pnr'+z+'.dat',"r")
        str1=f2.readline()
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MITS RAILWAYS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "                           arrival time : 11:55            departure time : 13:11"
        print "                           seat no:",ra
        print "                           class : 2AC"
        print "Name:",str1                                                             
        str2=f2.readline()
        print "Journey from station:",str2
        str3=f2.readline()
        print "To Station:",str3
        str4=f2.readline()
        print "DATE OF JOURNEY : ",str4
        str5=f2.readline()
        print "GENDER :",str5
      
        print "~~~~~~~~~~~~~~~~~~~~~~~HAPPY JOURNEY~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
  
 
def intro():
    print"_______________________________________________________________________"
    print "\n\t\t\tRAILWAY RESERVATION SYSTEM"
    print "\n\t\tMADE BY : AASHNA NAUSHAD & AAYSHA RASHEED"  

#Main function
intro()

a="SHRAILWAYS"
while a=="SHRAILWAYS":
  
        print"_______________________________________________________________________"
        print """MAIN MENU
 1. Passenger's DETAILS
 2. Passenger's reserved TICKET
 3. EXIT
    """
        ch=input("Enter Your Choice(1~3): ")
        if ch==1:
                pass_details()
        elif ch==2:
                display_passdetails()
        elif ch==3:
                cancel()
        else:
                break
else:
    print "Input correcr choice...(1-3)"
raw_input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")
 

