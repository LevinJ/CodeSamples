with open('/home/levin/workspace/snrprj/snr/data/banknotes/sample_test/batch_1/20171017162233/SN.txt', "rb") as f:
    byte = f.read(1)
    while byte != "":
        # Do stuff with byte.
        byte = f.read(1)
        print(byte)