
file = open("input.txt", "r")
message = file.readline()
testinput1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
testinput2 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"


def find_packet_marker(message: list):
    segment = []
    count = 1
    for char in message:
        segment.append(char)
        if len(segment) >= 4:
            if len(set(segment)) == 4:
                print(count)
                break
            segment.remove(segment[0])
        count += 1


def find_message(message: list):
    segment = []
    count = 1
    for char in message:
        segment.append(char)
        if len(segment) >= 14:
            if len(set(segment)) == 14:
                print(count)
                break
            segment.remove(segment[0])
        count += 1

# find_packet_marker(message)
find_message(message)
