# automatically generated by the FlatBuffers compiler, do not modify
from dataclasses import dataclass

@dataclass
{% set table_name = table.__name__ %}
class {{table_name}}:
{% for member, type in table['_fspec'].items() %}
{% set py_type = get_type(type[1]) %}
    {{member}}: {{py_type}}
{% endfor %}

