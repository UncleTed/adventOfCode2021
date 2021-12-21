

def shifting(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def pad_to_multiple_of_four(rest_of_packet):
    length = len(rest_of_packet)
    print(F'length: {length}')
    remainder = length % 4
    print(remainder)
    padded = rest_of_packet
    for i in range(remainder):
        padded.insert(0,0)
    print(padded)


def decode_packet(packet):
    version = shifting(list(map(int, '0' + packet[0:3])))
    type_id = shifting(list(map(int, '0' + packet[3:6])))
    rest_of_the_packet = packet[6:]
    packet_type = '??'
    if type_id == 4:
        packet_type = 'Literal'
    pad_to_multiple_of_four(list(map(int, rest_of_the_packet)))
    print(F'version: {version} type_id: {type_id} packet_type: {packet_type} the_rest: {rest_of_the_packet} has len(): {len(rest_of_the_packet)}')

def part1():
    with open("./short.txt") as f:
        for line in f:
            packet =  bin(int(line,16))[2:]
            decode_packet(packet)

part1()