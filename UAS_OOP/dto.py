from kink import inject
@inject
class DTO:
    def __init__(self, category, data):
        self.category = category
        self.data = data