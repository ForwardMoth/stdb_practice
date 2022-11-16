class ReadWriter:
    def formatted_print(self, columns):
        row = ""
        for i in columns:
            x = i
            if type(x) is not str:
                x = str(x)
            row += '{:<15}'.format(x)
        print(row)

    def read_next_step(self):
        return input("=> ").strip()