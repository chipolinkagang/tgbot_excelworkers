class States:
    is_add = False

    def true_add(self):
        self.is_add = True

    def false_add(self):
        self.is_add = False

    def get_add(self):
        return self.is_add


state = States()