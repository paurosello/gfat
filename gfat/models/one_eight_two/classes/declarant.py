from constants import DECLARANT_FIELDS
from one_eight_two.classes.base_class_182 import Base182


class Declarant(Base182):
    """Declarant Model"""

    def __init__(self):
        super(Declarant, self).__init__(DECLARANT_FIELDS)
        return
