from utils import formatters


class BaseClass(object):

    fields_meta = {}

    def __init__(self, fields_meta):
        self.fields_meta = fields_meta
        self.init_fields()

    def init_fields(self):
        for field in self.fields_meta:
            default_value = field.get("default", None)
            setattr(self, field["field_name"], default_value)

    def get_field_meta(self, field_name):
        return filter(lambda field: field['field_name'] == field_name, self.fields_meta)[0]

    def get_formatted_field(self, field_name):
        field_meta = self.get_field_meta(field_name)

        formatter = field_meta.get("formatter", formatters.fill_spaces)
        return formatter(self.__getattribute__(field_name), field_meta)
