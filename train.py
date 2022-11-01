import random

class Train:
    train_name="Hyderabad Express 17031"
    seats=200
    pnrlist=[]
    passenger_name=""
    passenger_age=0
    pnrno=0

    def __init__(self):
        print("\t\t\t\t\t********************************************\t\t\t\t")

        print(f"\t\t\t\t\t Train Name Is :{self.train_name}\t\t\t\t\t")
        print(f"\t\t\t\t\t Total Seats Are :{self.seats}\t\t\t\t\t")
        print(f"\t\t\t\t\t Available Seats Are :{self.seats}\t\t\t\t\t")

    def checkSeats(self):

        if(self.seats>1):
            return True
        else:
            return False

#book the ticket 
    def bookTicket(self):
              
        if(self.checkSeats()): 
            print("\t\t\t\t\t********************************************\t\t\t\t\t")

            seat=int(input("\t\t\t\t\t Enter How Many Seats You Want To Book: "))
            if(seat>self.seats):
                print(f"\t\t\t\t\t Only {self.seats} Seats Are Available...! \t\t\t\t\t")
                exit()
            else:    
                self.seats-=seat  
                for s in range(seat):
                    self.passenger_name=input(f"\t\t\t\t\t Enter Passenger {s+1} Name: ")
                    self.passenger_age=int(input(f"\t\t\t\t\t Enter Passenger {s+1} Age: "))
                    self.pnrno=random.randint(10000000,100000000)
                    self.pnrlist.append(self.pnrno) 
                    self.showPassengerDetails(self.pnrno,self.passenger_name,self.passenger_age)
            print("\t\t\t\t\t Tickets Booked Successfully. \t\t\t\t\t")


             
        else:
            print("\t\t\t\t\t Seats Are Full..! \t\t\t\t\t")

    def showPassengerDetails(self,pnrno,name,age):
        print(f"\t\t\t\t\t Your PNR Number Is :{pnrno} \t\t\t\t\t")
        print(f"\t\t\t\t\t Your Name Is :{name} \t\t\t\t\t")
        print(f"\t\t\t\t\t Your Age Is :{age} \t\t\t\t\t")
   
#cancel the ticket
    def cancelTicket(self):
        
        print("\t\t\t\t\t********************************************\t\t\t\t")
        ch=int(input("\t\t\t\t\t Enter How Many Ticket You Want To Delete: "))
        for c in range(ch):
            user_pnr=int(input(f"\t\t\t\t\t Plaese Enter Passenger {c+1} PNR Number To Delete The Ticket: "))
            return_res=self.checkpnrlist(user_pnr)
            if(return_res==False):
          
                print("\t\t\t\t\t PNR Number Does Not Exist. Please Enter Correct PNR Number. \t\t\t\t\t")
                user_pnr=int(input(f"\t\t\t\t\t Plaese Enter Passenger {c+1} PNR Number To Delete The Ticket: "))
                self.checkpnrlist(user_pnr)

#to check the pnr number in the pnr list
    def checkpnrlist(self,user_pnr):

        if user_pnr in self.pnrlist:
            self.seats+=1
            self.pnrlist.remove(user_pnr)
            print("\t\t\t\t\t Your Ticket is cancelled successfully.")
            return True
        else:
            return False

#main      
intercity=Train()
intercity.bookTicket()
intercity.cancelTicket()

