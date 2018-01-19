# func_value: gets value from a function without arguments
# length: field_length
# default: default value when initializing the field
# formatter: function that will format the field before printing
# mandatory: an error will be thrown if the field has no value

# DECLARANT
from utils import formatters

DECLARANT_FIELDS = [
    {"field_name": "register_type", "length": 1, "default": "1"},
    {"field_name": "declaration_model", "length": 3},
    {"field_name": "exercise", "length": 4},
    {"field_name": "declarant_id", "length": 9},
    {"field_name": "declarant_name", "length": 40, "func_value": "get_name"},
    {"field_name": "support_type", "length": 1},
    {"field_name": "contact_phone", "length": 9},
    {"field_name": "contact_name", "length": 40},
    {"field_name": "declaration_id", "length": 13},
    {"field_name": "complementing_declaration", "length": 1},
    {"field_name": "sustitutive_declaration", "length": 1},
    {"field_name": "last_declaration", "length": 13},
    {"field_name": "number_of_registers", "length": 9},
    {"field_name": "total_amount", "length": 15},
    {"field_name": "declarant_type", "length": 1},
    {"field_name": "protected_properties_declarant_id", "length": 9},
    {"field_name": "protected_properties_declarant_name", "length": 40},
    {"field_name": "blanks", "length": 28, "default": "", "formatter": formatters.fill_spaces},
    {"field_name": "electronic_signature", "length": 13}
]

# DECLARED
DECLARED_REGISTER_FIELDS = [
    {"field_name": "register_type", "length": 1, "default": "2"},
    {"field_name": "declaration_model", "length": 3},
    {"field_name": "exercise", "length": 4},
    {"field_name": "declaring_id", "length": 9},
    {"field_name": "declared_id", "length": 9},
    {"field_name": "representing_declared_id", "length": 9},
    {"field_name": "declared_name", "length": 40},
    {"field_name": "province_code", "length": 2},
    {"field_name": "key", "length": 1},
    {"field_name": "percentage_deduction", "length": 5},
    {"field_name": "amount", "length": 13},
    {"field_name": "in_kind_donation", "length": 1},
    {"field_name": "territory_deduction", "length": 2},
    {"field_name": "territory_deduction_percentage", "length": 5},
    {"field_name": "declared_type", "length": 1},
    {"field_name": "revocation", "length": 1},
    {"field_name": "revocation_date", "length": 4},
    {"field_name": "goods_type", "length": 1},
    {"field_name": "goods_identification", "length": 20},
    {"field_name": "donation_recurrence", "length": 1},
    {"field_name": "blanks", "length": 118, "formatter": formatters.fill_spaces}
]
