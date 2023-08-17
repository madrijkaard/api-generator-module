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

def generate_java_class(json_data, class_name):
    java_class = f"package com.mxs.model;\n\n"
    java_class += f"{get_imports(json_data)}\n\n"
    java_class += f"public class {class_name} {{\n\n"

    for key, value in json_data.items():
        java_type = get_java_type(value)
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]  # Converte a primeira letra para minúscula
        java_class += f"    private {java_type} {java_var_name};\n"

    # Empty constructor
    java_class += f"\n    public {class_name}() {{}}\n"

    # Constructor with all attributes
    java_class += f"\n    public {class_name}("
    constructor_params = ", ".join(f"{get_java_type(value)} {java_var_name}" for key, value in json_data.items())
    java_class += f"{constructor_params}) {{\n"
    for key in json_data.keys():
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]  # Converte a primeira letra para minúscula
        java_class += f"        this.{java_var_name} = {java_var_name};\n"
    java_class += "    }\n"

    # Getters and Setters
    for key, value in json_data.items():
        java_type = get_java_type(value)
        java_var_name = convert_to_camel_case(key)
        java_var_name = java_var_name[0].lower() + java_var_name[1:]  # Converte a primeira letra para minúscula
        java_getter_name = "get" + java_var_name[0].upper() + java_var_name[1:]  # Primeira letra do getter em maiúscula
        java_setter_name = "set" + java_var_name[0].upper() + java_var_name[1:]  # Primeira letra do setter em maiúscula
        java_class += f"\n    public {java_type} {java_getter_name}() {{\n"
        java_class += f"        return {java_var_name};\n"
        java_class += "    }\n"
        java_class += f"\n    public void {java_setter_name}({java_type} {java_var_name}) {{\n"
        java_class += f"        this.{java_var_name} = {java_var_name};\n"
        java_class += "    }\n"

    java_class += "}\n"
    return java_class

def get_java_type(value):
    if '.' in value:
        _, class_name = value.rsplit('.', 1)
        return class_name
    return ObjectType[value].value

def get_imports(json_data):
    imports = set()
    for value in json_data.values():
        if '.' in value:
            imports.add(value)
    return "\n".join(f"import {import_value};" for import_value in sorted(imports))

def main():
    input_directory = "in"
    output_directory = "out"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    input_files = [f for f in os.listdir(input_directory) if f.endswith(".json")]

    for input_file in input_files:
        with open(os.path.join(input_directory, input_file), 'r') as f:
            json_data = json.load(f)
        
        class_name = convert_to_camel_case(input_file.replace(".json", ""))
        class_name = class_name[0].upper() + class_name[1:]  # Primeira letra do nome da classe em maiúscula
        java_class = generate_java_class(json_data, class_name)
        
        output_file = os.path.join(output_directory, f"{class_name}.java")
        with open(output_file, 'w') as f:
            f.write(java_class)

if __name__ == "__main__":
    main()
