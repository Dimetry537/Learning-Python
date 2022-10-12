class File():

    def __init__(self, filename):
        self.filename = filename
        self.mode = 'a+'

    def __enter__(self):
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()

files = []
for _ in range(10000):
    with File('foo.txt') as infile:
        infile.write('foo')
        files.append(infile)