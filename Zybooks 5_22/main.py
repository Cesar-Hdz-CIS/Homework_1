# Cesar Hernandez 1835494

print("Davy's auto shop services\n"
      "Oil change -- $35\n"
      "Tire rotation -- $19\n"
      "Car wash -- $7\n"
      "Car wax -- $12\n")
Sum_services = 0
services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

first_service = str(input("Select first service:\n"))
Sum_services += services[first_service]
second_service = str(input("Select second service:\n"))
Sum_services += services[second_service]

print("\nDavy's auto shop invoice\n")

if not services[first_service] == 0:
    print("Service 1:", first_service + str(","), "$" + str(services[first_service]))
else:
    print('Service 1: No service')

if not services[second_service] == 0:
    print("Service 2:", second_service + str(","), "$" + str(services[second_service]))

else:
    print('Service 2: No service')

print("\nTotal: $" + str(Sum_services))

# print("Davy's auto shop invoice\n\n"
#      "Service 1:", first_service + str(","), "$" + str(services[first_service]),"\n"
#      "Service 2:", second_service + str(","), "$" + str(services[second_service]),"\n\n"
#      "Total: $" + str(Sum_services))