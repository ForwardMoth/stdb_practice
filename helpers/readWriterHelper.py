class ReadWriter:
    def __init__(self, columns=None):
        self.columns = columns

    def formatted_print(self):
        row = ""
        for i in self.columns:
            x = i
            if type(x) is not str:
                x = str(x)
            row += '{:<15}'.format(x)
        print(row)

    def read_next_step(self):
        return input("=> ").strip()