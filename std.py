import sys

# Check if 5 command-line values were provided
if len(sys.argv) == 6:
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
        n3 = int(sys.argv[3])
        n4 = int(sys.argv[4])
        n5 = int(sys.argv[5])
    except ValueError:
        print("ERROR: All inputs must be integers.")
        sys.exit(1)
else:
    print("NO input values - Using default values")
    n1, n2, n3, n4, n5 = 60, 80, 75, 60, 88

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
