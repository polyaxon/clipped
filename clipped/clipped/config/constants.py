import re


PARAM_REGEX = re.compile(r"{{\s*(.+)\s*}}", re.DOTALL)

NO_VALUE_FOUND = "_NO_VALUE_FOUND"
