class luggage :
    def _init_(self,luggage_id,luggage_weight,luggage_departure_airport,luggage_destination_airport,passenger_name):
            self.__luggage_id= luggage_id
            self.__luggage_weight= luggage_weight
            self.__luggage_departure_airport= luggage_departure_airport
            self.__luggage_destination_airport= luggage_destination_airport
            self.__passenger_name= passenger_name

 #行李ID的建構值
    def get_luggage_id(self):
        return self.__luggage_id

#行李重量的建構值
    def get_luggage_weight(self):
        return self.__luggage_weight

#行李出發機場的建構值
    def get_luggage_departure_airport(self):
        return self.__luggage_departure_airport

#行李目的地機場的建構值
    def get_luggage_destination_airport(self):
        return self.__luggage_destination_airport

#行李所屬旅客姓名的建構值
    def get_passenger_name(self):
        return self.__passenger_name

#主函式
    def main(): 
        c1=luggage("123","12kg","桃園機場","香港國際機場","lyh")
        d1=luggage("456","10kg","北京大興國際機場","深圳寶安國際機場","ysx")
        e1=luggage("789","15kg","澳門機場","北京大興國際機場","zls")

        print("行李ID1:",c1.get_luggage_id()) 
        print("行李重量1:",c1.get_luggage_weight())
        print("行李出發機場1:",c1.get_luggage_departure_airport())
        print("行李目的地機場1:",c1.get_luggage_destination_airport())
        print("行李所屬旅客姓名1:",c1.get_passenger_name())
        
        print("行李ID2:",d1.get_luggage_id()) 
        print("行李重量2:",d1.get_luggage_weight())
        print("行李出發機場2:",d1.get_luggage_departure_airport())
        print("行李目的地機場2:",d1.get_luggage_destination_airport())
        print("行李所屬旅客姓名2:",d1.get_passenger_name())
        
        print("行李ID3:",e1.get_luggage_id()) 
        print("行李重量3:",e1.get_luggage_weight())
        print("行李出發機場3:",e1.get_luggage_departure_airport())
        print("行李目的地機場3:",e1.get_luggage_destination_airport())
        print("行李所屬旅客姓名3:",e1.get_passenger_name())
       

class businesslicense :
    def _init_(self,businesslicense_name,businesslicense_number,boarding_passes,boarding_time,gate_number,seat_location,numberluggage_pieces,luggage_id):
            self.__businesslicense_name= businesslicense_name
            self.__boarding_passes= boarding_passes
            self.__boarding_time= boarding_time
            self.__gate_number= gate_number
            self.__seat_location= seat_location
            self.__numberluggage_pieces= numberluggage_pieces
            self.__luggage_id= luggage_id

 #旅客姓名的建構值
    def get_businesslicense_name(self):
        return self.__businesslicense_name

 #登機證編號的建構值
    def get_boarding_passes(self):
        return self.__boarding_passes
    
 #登機時間的建構值
    def get_boarding_time(self):
        return self.__boarding_time
    
 #登機門編號的建構值
    def get_gate_number(self):
        return self.__gate_number
    
 #座位位置的建構值
    def get_seat_location(self):
        return self.__seat_location
    
 #行李件數的建構值
    def get_numberluggage_pieces(self):
        return self.__numberluggage_pieces
    
 #行李ID的建構值
    def get_luggage_id(self):
        return self.__luggage_id
    
#主函式
    def main(): 
        h1=businesslicense("lyh","015","10:00am","abc1","a2","2件","123")
        i1=businesslicense("tjr","016","10:10am","abc2","a3","1件","124")
        j1=businesslicense("bl","017","10:15am","abc3","a2","3件","239")

        print("旅客機場1:",h1.get_luggage_id()) 
        print("登機證編號1:",h1.get_businesslicense_name()) 
        print("登機時間1:",h1.get_boarding_time()) 
        print("登機門編號1:",h1.get_gate_number()) 
        print("座位位置1:",h1.get_seat_location()) 
        print("行李件數1:",h1.get_numberluggage_pieces()) 
        print("行李ID1:",h1.get_luggage_id()) 

        print("旅客機場2:",i1.get_luggage_id()) 
        print("登機證編號2:",i1.get_businesslicense_name()) 
        print("登機時間2:",i1.get_boarding_time()) 
        print("登機門編號2:",i1.get_gate_number()) 
        print("座位位置2:",i1.get_seat_location()) 
        print("行李件數2:",i1.get_numberluggage_pieces()) 
        print("行李ID2:",i1.get_luggage_id()) 

        print("旅客機場3:",j1.get_luggage_id()) 
        print("登機證編號3:",j1.get_businesslicense_name()) 
        print("登機時間3:",j1.get_boarding_time()) 
        print("登機門編號3:",j1.get_gate_number()) 
        print("座位位置3:",j1.get_seat_location()) 
        print("行李件數3:",j1.get_numberluggage_pieces()) 
        print("行李ID3:",j1.get_luggage_id()) 

    if __name__ == "__main__":
        main()