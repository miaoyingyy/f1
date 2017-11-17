def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
    print"ok"

try:
    fuctionName(4)                
except "Invalid level!":
    print "user defined exception"
else:
    print "else"
finally:
    print"finally always run....."

