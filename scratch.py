# simple inquiry example
import bluetooth



file='received_bin.bin'
with open(file,'rb') as bin:
    with open("received_hex",'w+') as hex:
        hex.write(bin.read().hex())
