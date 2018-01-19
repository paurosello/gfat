from base_class import BaseClass


class Base182(BaseClass):
    def get_representation(self):
        representation = ""
        for field in self.fields_meta:
            representation += self.get_formatted_field(field["field_name"])

        return representation
