import argparse
import math
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        action='store',
        help="un nombre positif",
        required=True,
        type=float
    )
    args = parser.parse_args()

    if args.number < 0:
        error = "le nombre \" "+str(args.number) + "\" <=0. Operation impossible."
        sys.stderr.write(error)
        raise ValueError(error)

    try:
        print(math.log(args.number))
    except ValueError :
        print("le nombre \" "+str(args.number) + "\" <=0. Operation impossible.", file=sys.stderr)