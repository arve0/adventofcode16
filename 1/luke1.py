coordinates = [(0,0)]

currentx = 0
currenty = 0

facing = 0 # N, E, S, W => 0, 1, 2, 3
found_twice = False


def find_path(dir):
    global facing, currentx, currenty, found_twice
    steps = int(dir[1:])
    if dir[0] == "R":
        facing = ((facing + 1 + 4) % 4)
    else:
        facing = ((facing - 1 + 4) % 4)

    if facing == 0:
        for i in xrange(1, steps + 1):
            coordinate = (currentx, currenty + i)
            if coordinate not in coordinates:
                coordinates.append(coordinate)
            elif not found_twice:
                found_twice = True
                print "Twice:", abs(currentx) + abs(currenty + i)
        currenty += steps

    elif facing == 1:
        for i in xrange(1, steps + 1):
            coordinate = (currentx + i, currenty)
            if coordinate not in coordinates:
                coordinates.append(coordinate)
            elif not found_twice:
                found_twice = True
                print "Twice:", abs(currentx + i) + abs(currenty)
        currentx += steps
    elif facing == 2:
        for i in xrange(1, steps + 1):
            coordinate = (currentx, currenty - i)
            if coordinate not in coordinates:
                coordinates.append(coordinate)
            elif not found_twice:
                found_twice = True
                print "Twice:", abs(currentx) + abs(currenty - i)
        currenty -= steps

    elif facing == 3:
        for i in xrange(1, steps + 1):
            coordinate = (currentx - i, currenty)
            if coordinate not in coordinates:
                coordinates.append(coordinate)
            elif not found_twice:
                found_twice = True
                print "Twice:", abs(currentx - i) + abs(currenty)
        currentx -= steps




def main():
    map = []
    file = open("input.py","r")
    data = file.readlines()

    for line in data:
        words = line.split(",")
        for word in words:
            map.append(word.strip())

    for i in range(len(map)):
        find_path(map[i])
    print "Last destination:",currentx, currenty
    print "Distance:", abs(currentx) + abs(currenty)
#    print coordinates

if __name__ == '__main__':
    main()
