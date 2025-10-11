H = float(input("Enter High: "))
print("High is:", H)

L = float(input("Enter Low: "))
print("Low is:", L)

C = float(input("Enter Close: "))
print("Close is:", C)

Pivot = (H + L + C) / 3
print("Pivot: {:.2f}".format(Pivot))

R1 = (2 * Pivot) - L
print("Resistance 1: {:.2f}".format(R1))

S1 = (2 * Pivot) - H
print("Support 1: {:.2f}".format(S1))

X = H - L
R2 = Pivot + X
print("Resistance 2: {:.2f}".format(R2))

S2 = Pivot - X
print("Support 2: {:.2f}".format(S2))

R3= H + 2*(Pivot-L)
print("Resistance 3: {:.2f}".format(R3))

S3 = L - 2*(H-Pivot)
print("Support 3: {:.2f}".format(S3))



