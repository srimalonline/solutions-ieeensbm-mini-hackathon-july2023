# Input Handling
[b, f] = [int(a) for a in input().split()]
[bp, fp] = [int(a) for a in input().split()]

total_bus_fare = 3*((b*(bp+100))/100)
total_bike_cost = ((((f*(fp+100))/100)/40)*26) + (700/90)

if(total_bike_cost-20 > total_bus_fare):
    print("Travel by bus")
else:
    print("Travel by bike")