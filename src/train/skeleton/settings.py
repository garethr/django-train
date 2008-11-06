ENV = "development"

try:
    exec "from environments." + ENV + " import *"
except ImportError:
    print "You must specify a valid environment"
    exit()