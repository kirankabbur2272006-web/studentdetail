import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    n4 = int(sys.argv[4])
    n5 = int(sys.argv[5])
else:
    print("NO input values - Using default values")
    script_name = sys.argv[0]
    n1 = 60
    n2 = 80
    n3 = 75
    n4 = 60
    n5 = 88

avg = (n1 + n2 + n3 + n4 + n5) / 5
print(f"Average is: {avg}")

if avg > 90:
    print("A grade")
elif avg > 80:
    print("B grade")
elif avg > 70:
    print("C grade")
elif avg > 60:
    print("D grade")
elif avg > 50:
    print("E grade")
else:
    print("FAIL")
