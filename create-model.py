import os
import json
from enum import Enum

class ObjectType(Enum):
    byte = 'byte'
    short = 'short'
    int = 'int'
    long = 'long'
    float = 'float'
    double = 'double'
    char = 'char'
    boolean = 'boolean'
    Object = 'Object'
    String = 'String'
    Integer = 'Integer'
    Long = 'Long'
    Double = 'Double'
    Float = 'Float'
    Character = 'Character'
    Boolean = 'Boolean'
    java_util_UUID = 'java.util.UUID'
    java_math_BigDecimal = 'java.math.BigDecimal'
    java_util_ArrayList = 'java.util.ArrayList'
    java_util_LinkedList = 'java.util.LinkedList'
    java_util_HashSet = 'java.util.HashSet'
    java_util_TreeSet = 'java.util.TreeSet'
    java_util_HashMap = 'java.util.HashMap'
    java_util_LinkedHashMap = 'java.util.LinkedHashMap'
    java_util_LinkedHashSet = 'java.util.LinkedHashSet'
    java_util_PriorityQueue = 'java.util.PriorityQueue'
    java_util_Stack = 'java.util.Stack'
    java_util_Queue = 'java.util.Queue'
    java_util_Deque = 'java.util.Deque'
    java_util_List = 'java.util.List'
    java_util_Map = 'java.util.Map'
    java_util_Set = 'java.util.Set'
    java_time_LocalDate = 'java.time.LocalDate'
    java_time_LocalTime = 'java.time.LocalTime'
    java_time_LocalDateTime = 'java.time.LocalDateTime'
    java_time_ZonedDateTime = 'java.time.ZonedDateTime'
    java_time_Instant = 'java.time.Instant'
    java_time_Duration = 'java.time.Duration'
    java_time_Period = 'java.time.Period'
    java_time_format_DateTimeFormatter = 'java.time.format.DateTimeFormatter'
    java_time_format_DateTimeParseException = 'java.time.format.DateTimeParseException'
    java_time_temporal_TemporalAdjusters = 'java.time.temporal.TemporalAdjusters'
    java_time_zone_ZoneId = 'java.time.zone.ZoneId'
    java_time_zone_ZoneOffsetTransition = 'java.time.zone.ZoneOffsetTransition'
    java_time_zone_ZoneRules = 'java.time.zone.ZoneRules'

def convert_to_camel_case(snake_case):
    words = snake_case.split('_')
    return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(words))

def generate_field_declaration(field_name, field_type):
    if field_type.startswith('java.util.'):
        collection_type = field_type.split('.')[-1]
        return f"private {collection_type}<{get_java_type(field_type['of']['value'])}> {field_name};"
    else:
        return f"private {field_type} {field_name};"

def generate_getter_and_setter(field_name, field_type):
    getter_name = "get" + field_name[0].upper() + field_name[1:]
    setter_name = "set" + field_name[0].upper() + field_name[1:]
    
    if field_type.startswith('java.util.'):
        collection_type = field_type.split('.')[-1]
        element_type = get_java_type(field_type['of']['value'])
        getter = f"public {collection_type}<{element_type}> {getter_name}() {{\n    return {field_name};\n}}"
        setter = f"public void {setter_name}({collection_type}<{element_type}> {field_name}) {{\n    this.{field_name} = {field_name};\n}}"
    else:
        getter = f"public {field_type} {getter_name}() {{\n\t    return {field_name};\n\t}}"
        setter = f"public void {setter_name}({field_type} {field_name}) {{\n\t    this.{field_name} = {field_name};\n\t}}"
    
    return getter, setter

def generate_constructor_parameters(json_data):
    params = []
    for key, value in json_data.items():
        java_type = get_java_type(value)
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]
        params.append(f"{java_type} {java_var_name}")
    return ", ".join(params)

def generate_imports(json_data):
    imports = set()
    for value in json_data.values():
        if isinstance(value, dict):
            if 'type' in value:
                imports.add(value['type'])
        elif '.' in value:
            imports.add(value)
    return "\n".join(f"import {import_value};" for import_value in sorted(imports))

def generate_java_class(json_data, class_name, main_package):
    java_class = f"package {main_package}.model;\n\n"
    java_class += f"{generate_imports(json_data)}\n\n"
    java_class += f"public class {class_name}Model {{\n\n"

    for key, value in json_data.items():
        java_type = get_java_type(value)
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]
        java_class += f"    {generate_field_declaration(java_var_name, java_type)}\n"

    java_class += f"\n    public {class_name}Model() {{}}\n"

    constructor_params = generate_constructor_parameters(json_data)
    java_class += f"\n    public {class_name}Model({constructor_params}) {{\n"
    for key in json_data.keys():
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]
        java_class += f"        this.{java_var_name} = {java_var_name};\n"
    java_class += "    }\n"

    for key, value in json_data.items():
        java_type = get_java_type(value)
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]
        
        getter, setter = generate_getter_and_setter(java_var_name, java_type)
        
        java_class += f"\n    {getter}\n"
        java_class += f"\n    {setter}\n"

    java_class += "}\n"
    return java_class

def get_java_type(value):
    if isinstance(value, dict):
        if 'type' in value and 'of' in value:
            collection_type = value['type'].split('.')[-1]
            element_type = get_java_type(value['of']['value'])
            return f"{collection_type}<{element_type}>"
    elif '.' in value:
        _, class_name = value.rsplit('.', 1)
        return class_name
    return ObjectType[value].value

def main():
    config_file_path = "config/main.json"

    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)

    project_name = config_data["project-name"]
    main_package = config_data["main-package"]
    
    input_directory = "in"
    output_base_directory = "out"
    output_directory = os.path.join(output_base_directory, project_name, "src/main/java", main_package.replace(".", "/"), "model")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    input_files = [f for f in os.listdir(input_directory) if f.endswith(".json")]

    for input_file in input_files:
        with open(os.path.join(input_directory, input_file), 'r') as f:
            json_data = json.load(f)
        
        class_name = convert_to_camel_case(input_file.replace(".json", ""))
        class_name = class_name[0].upper() + class_name[1:]
        java_class = generate_java_class(json_data, class_name, main_package)
        
        output_file = os.path.join(output_directory, f"{class_name}Model.java")
        with open(output_file, 'w') as f:
            f.write(java_class)

if __name__ == "__main__":
    main()