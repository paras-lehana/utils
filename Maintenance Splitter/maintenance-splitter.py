# Program to generate maintenance bill for each individual in the flat

import math;                   

print('\n\n---------  Maintenance Splitter  ---------\n\n');

UNIT_RATE = 7.70;   # Cost per Electricity Unit
print('Grid Unit Rate: ₹ ', UNIT_RATE, '\n');

rooms = [ ['Paras'], ['Ayushmaan'], ['Abhinav'] ];    # List of Rooms with nested list of members in each room

print('Rooms: ', end='');
[print('| ' + ', '.join(members) + ' |', end='') for members in rooms];
print('\n\n');

current_bill = float(input('Current - Previous Bill: '))   # Current Total Bill of the month
print('\n');

bill = {}; # Bill of each flat member

total_ac_bill = 0; # Total AC Cost consumed by flat


for members in rooms: #runs for each room

    current_room_ac_units, *previous_room_ac_units = input('Current - Previous AC units reading for Room of ({}): '.format(', '.join(members))).split('-'); #required format current-previous, previous can be omitted and defaults to 0
    previous_room_ac_units = previous_room_ac_units[0] if previous_room_ac_units else 0;
    room_ac_units = float(current_room_ac_units)-float(previous_room_ac_units)  

    room_ac_bill = room_ac_units * UNIT_RATE;    #AC Cost consumed by the room
    print('Consumed AC Units: {} Units -> ₹ {}'.format(room_ac_units, room_ac_bill));


    for member in members:  #runs for each member in the room
        bill[member] = math.ceil(room_ac_bill/len(members)); #AC bill is divided by room occupancy; The dict bill contains the member_name -> amount_to_be_paid  
    
    total_ac_bill += room_ac_bill;


common_bill = (current_bill - total_ac_bill); #Common Bill (without AC) is divided equally among flat members

print ('\nCurrent Bill: ₹', current_bill);
print ('Common Bill: ₹ {} (₹ {} per head)'.format(common_bill, common_bill/len(bill)))
print ('AC Bill: ₹', total_ac_bill);

print ('\n\nIndividual Bills:\n');
round_current_bill = 0

for name, ac_amount in bill.items():

    member_amount = ac_amount + common_bill/len(bill);    #Common Bill share added to each member
    print ('{}: ₹ {} (including ₹ {} AC)'.format(name, math.ceil(member_amount), ac_amount)); # Outputting member name and amount to be paid
    round_current_bill += member_amount

print('\n\nRounded Off Total Bill: ', round_current_bill,'\n\n')