import sys
import os

cwd = os.path.dirname(os.path.abspath(__file__))
append_path = cwd + "/../lib"

sys.path.append(append_path)
import jjl_3d as _3d


def main(argv):
    p = _3d.Point2D()
    p.print()
    exit(0)

if __name__ == "__main__":
    main( sys.argv )