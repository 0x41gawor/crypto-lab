import math
import argparse
# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('x', type=int,
                    help='A required integer positional argument')
args = parser.parse_args()
x = args.x

counter = 0
for i in range(1,x):
    if (math.gcd(x,i) == 1):
        counter += 1
print(f"Totien of {x}: {counter}")