import math


def fizzBuzz(n: int) -> None:

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))

def paginate_generator(data, page_size):

    total_data = len(data)
    for i in range(0, total_data, page_size):
        yield data[i:i + page_size]




for x in paginate_generator([1,2,3,4,5,6], 2):
    print(x)



averageUtil = [25,23,1,2,3,4,5,6,7,8,9,10,76,80]

def finalInstance(instances, averageUtil):

    i = 0 
    while i < len(averageUtil):

        
        if averageUtil[i] < 25:
            if instances > 1:
                instances = math.ceil(instances/2) 
                i += 10
            else:
                i += 1
        elif averageUtil[i] > 60:
            if instances * 2 <= 2 * 10**8:
                instances = instances * 2
                i += 10
            else:
                i += 1
        else:
            i += 1
    
    return instances

finalInstance(1,  [25,23,1,2,3,4,5,6,7,8,9,10,76,80])
finalInstance(1,  [1,3,5,10,80])




def hashed_ports(numberOfPorts, transmissionTime, packetIds):

    ports = [0] * numberOfPorts
    ans = [0] * len(packetIds)


    for i, packet_id in enumerate(packetIds):
        time = i+1
        port = packet_id % numberOfPorts
        
        for _ in range(numberOfPorts):
            if ports[port] <= time: 
                ans[i] = port
                ports[port] = time + transmissionTime 
                break
            else:
                port = (port + 1) % numberOfPorts
    
    return ans

numberOfPorts = 3
transmissionTime = 2
packetIds = [4, 7, 10, 6]
print(hashed_ports(numberOfPorts, transmissionTime, packetIds))

print(hashed_ports(numberOfPorts, transmissionTime, packetIds))
