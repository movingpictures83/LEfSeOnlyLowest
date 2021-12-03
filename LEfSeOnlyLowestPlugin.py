import sys

class LEfSeOnlyLowestPlugin:
    def input(self, filename):
        self.resfile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
        outresfile = open(filename, 'w')

        lines = []

        for line in self.resfile:
           contents = line.split('\t')
           flag = False
           taxon = contents[0]
           toRemove = []
           flag = False
           if (len(contents[2])>0):
            for line2 in lines:
               contents2 = line2.split('\t')
               taxon2 = contents2[0]
               if (taxon.startswith(taxon2) and len(contents[2])>0):
                  toRemove.append(line2)
               elif taxon2.startswith(taxon):
                   flag = True
                   break
           if not flag:
               lines.append(line)
           for element in toRemove:
               lines.remove(element)

        for line in lines:
            outresfile.write(line)
