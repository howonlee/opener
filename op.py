import sys
from subprocess import call

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "put in an argument"
        sys.exit(1)
    for filename in sys.argv[1:]:
        ext = filename.rpartition(".")[-1]
        print "found a ", ext, " file. Trying to open..."
        if ext in ["pdf"]:
            print "opening pdf..."
            call(["mupdf", filename])
        elif ext in ["jpeg", "jpg", "png"]:
            print "opening picture with feh..."
            call(["feh", filename])
        elif ext in ["gif"]:
            print "opening gif with gifview..."
            call(["gifview", filename])
        elif ext in ["svg"]:
            print "opening svg with inkscape..."
            call(["inkscape", filename])
        elif ext in ["doc", "docx", "xls", "xlsx", "ppt",
                "pptx", "rtf", "odt", "fodt", "ods", "fods",
                "odp", "fodp", "odb", "odg", "fodg", "odf"]:
            print "opening officey format with libreoffice..."
            call(["libreoffice", filename])
        elif ext in ["wav", "mp3", "ogg"]:
            print "opening sound file with mplayer..."
            call(["mplayer", filename])
        else:
            print "I don't recognize this file"
