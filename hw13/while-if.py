nucleotide = ""
while(nucleotide != "X"):
    nucleotide = raw_input("INput X for exit, nucleotide A, C, T, G:")
    print nucleotide

    if nucleotide == "A":
        print "ADENINA"
    elif nucleotide == "C":
        print "CITOSINA"
    elif nucleotide == "G":
        print "GUANINA"
    elif nucleotide == "T":
        print "TIMINA"
    elif nucleotide == "X":
        print "Bye.."
    else:
        print "ERROR In input"




