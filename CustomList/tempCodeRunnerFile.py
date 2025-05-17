if self.array[i] == value:
                found = True
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                break