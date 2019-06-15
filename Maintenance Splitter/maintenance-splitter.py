# Program to generate maintenance bill for each individual in the flat

import math;                   

print('Maintenance Splitter');

UNIT_RATE = 6.98;   #Cost per Electricity Unit

rooms = [ ['Paras','Ayushmaan'], ['Divyank'], ['Harshit','Manik'] ];    #List of Rooms with nested list of members in each room

current_bill = float(input('Current - Previous Bill: '))   #Current Total Bill of the month
bill = {}; #Bill of each flat member

total_ac_bill = 0; #Total AC Cost consumed by flat


for members in rooms: #runs for each room

    current_room_ac_units, *previous_room_ac_units = input('Current - Previous AC units reading for Room of ({}): '.format(', '.join(members))).split('-'); #required format current-previous, previous can be omitted and defaults to 0
    previous_room_ac_units = previous_room_ac_units[0] if previous_room_ac_units else 0;
    print('Consumed AC Units:',float(current_room_ac_units)-float(previous_room_ac_units),'\n');    

    room_ac_bill = ( float(current_room_ac_units) - float(previous_room_ac_units) ) * UNIT_RATE;    #AC Cost consumed by the room

    for member in members:  #runs for each member in the room
        bill[member] = room_ac_bill/len(members); #AC bill is divided by room occupancy; The dict bill contains the member_name -> amount_to_be_paid  
    
    total_ac_bill += room_ac_bill;


common_bill = (current_bill - total_ac_bill); #Common Bill (without AC) is divided equally among flat members

print ('\nCurrent Bill: ₹',current_bill);
print ('Common Bill: ₹',common_bill);

print ('\n\nIndividual Bills:');

for name, amount in bill.items():
    amount += common_bill/len(bill);    #Common Bill share added to each member
    print ('{}: ₹ {}'.format(name,math.ceil(amount))); #Outputting member name and amount to be paid