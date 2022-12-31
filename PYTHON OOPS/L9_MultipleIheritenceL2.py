class dad:
    basketball = 1

class son(dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes i dance {self.dance} no of times"

class grandson(son):
    dance = 6
    def isdance(self):
        return f"Yes i dance very awesome {self.dance} no of times"

if __name__ == '__main__':
    darry = dad()
    larry = son()
    harry = grandson()

    # print(harry.isdance())
    print(harry.basketball)