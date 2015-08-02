import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "put in an argument"
        sys.exit(1)
    filename = sys.argv[1]
    if filename[:4] == ".pdf":
        put out evince for this shit
    elif filename[:4] in [".jpg", ".png", ".gif", other shit]:
        put out feh for this shit
