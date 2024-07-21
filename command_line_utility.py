import argparse

parser=argparse.ArgumentParser()

# add command line arguments
parser.add_argument("arg1", help="description of argument 1 ")
parser.add_argument("arg2",help="description of argument 2")

# parse the arguments
args=parser.parse_args()

# use the arguments in your code
print(args.arg1)
print(args.arg2)