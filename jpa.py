import os
import json
import re

config_file_path = "config/main.json"

# Lê o arquivo JSON para obter o valor do atributo "main-package"
with open(config_file_path, 'r') as json_file:
    data = json.load(json_file)
    project_name = data["project-name"]
    main_package = data['main-package']

output_base_directory = "out"
model_dir = os.path.join(output_base_directory, project_name, "src/main/java", main_package.replace(".", "/"), "model")

# Expressão regular para encontrar a definição de classe
class_pattern = re.compile(r'^\s*public\s+class\s+(\w+)Model\s+{', re.MULTILINE)
attribute_pattern = re.compile(r'^\s*(private\s+\w+\s+(\w+);)', re.MULTILINE)

# Verifica a versão do Spring Boot no arquivo "pom.xml"
pom_xml_path = os.path.join(output_base_directory, project_name, "pom.xml")
with open(pom_xml_path, 'r') as pom_file:
    pom_content = pom_file.read()
    if "<version>2" in pom_content:
        import_statement = "import javax.persistence.*;"
    elif "<version>3" in pom_content:
        import_statement = "import jakarta.persistence.*;"
    else:
        import_statement = ""

# Percorre todos os arquivos no diretório "model"
for filename in os.listdir(model_dir):
    if filename.endswith('.java'):
        file_path = os.path.join(model_dir, filename)
        
        # Lê o conteúdo do arquivo
        with open(file_path, 'r') as java_file:
            java_code = java_file.read()
        
        # Encontra o nome da classe usando a expressão regular
        match_class = class_pattern.search(java_code)
        if match_class:
            class_name = match_class.group(1)

            # Converte o nome da classe para minúsculas e remove o sufixo "Model"
            entity_name = class_name.lower().replace("model", "")
            
            # Adiciona o import apropriado abaixo do package
            package_declaration = f"package {main_package}.model;\n"
            import_statement_with_package = package_declaration + "\n" + import_statement
            
            # Substitui o package e adiciona o import
            java_code = java_code.replace(package_declaration, import_statement_with_package, 1)

            # Adiciona o import "import org.hibernate.annotations.GenericGenerator;"
            if "import jakarta.persistence.*;" in java_code:
                java_code = java_code.replace("import jakarta.persistence.*;", "import jakarta.persistence.*;\nimport org.hibernate.annotations.GenericGenerator;")
            
            # Adiciona a anotação @Entity acima da definição da classe
            entity_annotation = f'\n@Entity(name = "{entity_name}")'
            java_code = class_pattern.sub(entity_annotation + match_class.group(0), java_code)

            # Encontra os atributos usando a expressão regular
            attributes = attribute_pattern.findall(java_code)
            
            if attributes:
                # Atualiza o código Java com as anotações @Column
                updated_code = java_code

                # Adiciona o atributo "id" no início da lista de atributos
                id_annotation = '@Id\n\t@GeneratedValue(generator = "increment")\n\t@GenericGenerator(name = "increment", strategy = "increment")\n\tprivate Long id;'
                updated_code = updated_code.replace(attributes[0][0], id_annotation + '\n\t' + attributes[0][0], 1)

                for attribute, attribute_name in attributes:
                    column_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', attribute_name).lower()
                    column_annotation = f'@Column(name = "{column_name}")\n\t{attribute}'
                    updated_code = updated_code.replace(attribute, column_annotation, 1)

                # Escreve o código Java modificado de volta para o arquivo
                with open(file_path, 'w') as java_file:
                    java_file.write(updated_code)






