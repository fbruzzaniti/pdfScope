import sys, hashlib

def sha1(filename):

    # Open file and read contents
    f = open(filename, 'rb')
    m = hashlib.sha1()
    m.update(f.read())
    f.close()
 
    # Create SHA1 hash
    sha1 = m.hexdigest()

    return sha1

def sha256(filename):

    # Open file and read contents
    f = open(filename, 'rb')
    m = hashlib.sha256()
    m.update(f.read())
    f.close()
 
    # Create SHA1 hash
    sha256 = m.hexdigest()

    return sha256


def md5(filename):

    # Open file and read contents
    f = open(filename, 'rb')
    m = hashlib.md5() 
    m.update(f.read())
    f.close()

    # Create MD5 hash
    md5 = m.hexdigest()
    
    return md5

#print 'File: ' + sys.argv[1] + "\n"
print 'MD5: ' + md5(sys.argv[1]) + "\n"
print 'SHA1: ' + sha1(sys.argv[1]) + "\n"
print 'SHA256: ' + sha256(sys.argv[1]) + "\n"

