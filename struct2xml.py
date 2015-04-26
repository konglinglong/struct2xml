import os
def GetProcFile(path):
    newfilelist = []
    filelist = os.listdir(path)
    for filename in filelist:
        if os.path.splitext(filename)[1] == ".h":
            #print(filename)
            newfilelist.append(filename)
    return newfilelist

def IsStructBegin(textline):
    if 'struct' in textline:
        return True
    else:
        return False
        
def IsStructEnd(textline):
    if '}' in textline:
        return True
    else:
        return False
        
def FileProc(filename):
    file = open(filename)
    textlist = file.readlines()
    for line in textlist:
        if IsStructBegin(line):
            print(line)
        elif IsStructEnd(line):
            print(line)
            

if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    filelist = GetProcFile(basedir)
    for filename in filelist:
        FileProc(filename)