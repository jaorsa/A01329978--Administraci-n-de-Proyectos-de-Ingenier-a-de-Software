adnseq  = ["A", "C", "T", "G", "A", "T", "G", "T", "A", "C"]
adnseq2 = ["T", "G", "A", "T", "G"]

n = len(adnseq)
print adnseq
print " length =",n

print "inserting one item.."
adnseq.append("T")
print adnseq
print "new length =", len(adnseq)

print "replace first position with T"
adnseq[0] = "T"
print adnseq

print "delete last position.."
adnseq.pop(-1)
print adnseq

print "newadnseq = seq1 + seq2"
newadnseq = adnseq + adnseq2

print adnseq
print adnseq2
print newadnseq
print "length =", len(newadnseq)

