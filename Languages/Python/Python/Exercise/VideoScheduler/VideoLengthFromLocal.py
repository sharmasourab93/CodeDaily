import subprocess
def getLength(o):
    result = subprocess.Popen(["ffprobe", o],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    return [x for x in result.stdout.readlines() if "Duration" in x]
def main():
    obj='file:\\\\C:\\Users\\ESOUSSH\\Desktop\\Digital Signage\\Wildlife.wmv'
    getLength(obj)
main()
