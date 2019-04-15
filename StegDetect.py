
import getopt
import os
from PIL import Image
import sys
from time import time


def show_lsb(image_path, n):
    """Shows the n least significant bits of image"""
    start = time()
    image = Image.open(image_path)

    # Used to set everything but the least significant n bits to 0 when
    # using bitwise AND on an integer
    mask = ((1 << n) - 1)

    color_data = [(255 * ((rgb[0] & mask) + (rgb[1] & mask) + (rgb[2] & mask))
                   // (3 * mask),) * 3 for rgb in image.getdata()]

    image.putdata(color_data)
    print("Runtime: {0:.2f} s".format(time() - start))
    file_name, file_extension = os.path.splitext(image_path)
    image.save(file_name + "_{}LSBs".format(n) + file_extension)


def usage():
    print("\nCommand Line Arguments:\n",
          "-f, --file=       Path to an image\n",
          "-n, --LSBs=       How many LSBs to display\n",
          "--help            Display this message\n")


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:n:',
                                   ['file=', 'LSBs=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(1)

    # file paths for input file
    input_fp = ""

    # number of least significant bits to display
    num_bits = 2

    for opt, arg in opts:
        if opt in ("-f", "--file"):
            input_fp = arg
        elif opt in ("-n", "--LSBs="):
            num_bits = int(arg)
        elif opt == "--help":
            usage()
            sys.exit(1)
        else:
            print("Invalid argument {}".format(opt))

    try:
        show_lsb(input_fp, num_bits)
    except Exception as e:
        print("Ran into an error during execution.\n",
              "Check input and try again.\n")
        print(e)
        usage()
        sys.exit(1)
