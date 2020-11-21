import heapq

class Parkinglot:
    """
    parkingLotCapacity: int: Total Number of vehicles that can be parked
    vacantSlots: list[int]: Empty slots available
    slots: list[list[int]]: stores [vehicle number, driver age] for a given slot
    driverAges: list[list[int]]: stores [slot, vehicle number] for a driver age
    slotVehicleMap: dict: stores slot for a vehicle number
    """

    def __init__(self):
        self.parkingLotCapacity = -1
        self.vacantSlots = []
        self.slots = [[] for i in range(1001)]
        self.driverAges = [[] for i in range(1001)]
        self.slotVehicleMap = {}

    """
    args:
        parkingLotCapacity: int
    return:
        string
    """
    def setCapacity(self, parkingLotCapacity):
        self.parkingLotCapacity = parkingLotCapacity
        for i in range(1, self.parkingLotCapacity + 1):
            self.vacantSlots.append(i)
        heapq.heapify(self.vacantSlots)
        return "Created parking of {} slots".format(parkingLotCapacity)

    """
    args:
        driverAge: int
        vehicleNumber: string
    return:
        string
    """
    def parkVehicle(self, driverAge, vehicleNumber):
        if self.parkingLotCapacity < 0:
            return "Parking lot space is not allocated yet."

        if len(self.vacantSlots) == 0:
            return "Cannot park more vehicles. Sorry!!!"

        availableSlot = heapq.heappop(self.vacantSlots)
        self.driverAges[driverAge].append([availableSlot, vehicleNumber])
        self.slots[availableSlot] = [vehicleNumber, driverAge]
        self.slotVehicleMap[vehicleNumber] = availableSlot

        return "Car with vehicle registration number {} has been parked at slot number {}".format(vehicleNumber, availableSlot)

    """
    args:
        driverAge: int
    return:
        string
    """
    def getSlotsWithDriverAge(self, driverAge):
        slots = []
        for slot, vehicleNumber in self.driverAges[driverAge]:
            slots.append(str(slot))
        return ','.join(slots)

    """
    args:
        vehicleNumber: string
    return:
        string
    """
    def getSlotForVehicleNumber(self, vehicleNumber):
        return self.slotVehicleMap.get(vehicleNumber, "No vehicle is parked with these details.")


    """
    args:
        slot: int
    return:
        string
    """
    def vacateSlot(self, slot):
        if slot < 1 or slot > self.parkingLotCapacity:
            return "There is no such slot. Are you sure?"

        if self.slots[slot] == []:
            return "Slot is already vacant."

        vehicleNumber, driverAge = self.slots[slot]

        self.slots[slot] = []

        for i in range(len(self.driverAges[driverAge])):
            if self.driverAges[driverAge][i][0] == slot:
                self.driverAges[driverAge].pop(i)
                break

        self.slotVehicleMap.pop(vehicleNumber)

        heapq.heappush(self.vacantSlots, slot)

        return "Slot number {} vacated, the car with vehicle registration number {} left the space, the driver of the car was of age {}".format(slot, vehicleNumber, driverAge)

    """
    args:
        driverAge: int
    return:
        string
    """
    def getCarsWithDriverAge(self, driverAge):
        cars = []
        for slot, vehicleNumber in self.driverAges[driverAge]:
            cars.append(vehicleNumber)
        return ','.join(cars)


def main():
    parkingLot = Parkinglot()
    input = open("./input.txt")

    for line in input:
        line = line.lstrip().rstrip()
        try:
            command = line.split()
            action = command[0]

            if action == "Create_parking_lot":
                print(parkingLot.setCapacity(int(command[1])))

            elif action == "Park" and command[2] == "driver_age":
                vehicleNumber = command[1]
                driverAge = int(command[3])
                print(parkingLot.parkVehicle(driverAge, vehicleNumber))

            elif action == "Slot_numbers_for_driver_of_age":
                driverAge = int(command[1])
                print(parkingLot.getSlotsWithDriverAge(driverAge))

            elif action == "Leave":
                slot = int(command[1])
                print(parkingLot.vacateSlot(slot))

            elif action == "Slot_number_for_car_with_number":
                vehicleNumber = command[1]
                print(parkingLot.getSlotForVehicleNumber(vehicleNumber))

            elif action == "Vehicle_registration_number_for_driver_of_age":
                driverAge = int(command[1])
                print(parkingLot.getCarsWithDriverAge(driverAge))

            else:
                print("Ohh!! This command is out of my syllabus. I am still learning.")
        except:
            print('Something went wrong with command -> ' + line)


if __name__ == "__main__":
    main()
