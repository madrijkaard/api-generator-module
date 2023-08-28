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
        match = class_pattern.search(java_code)
        if match:
            class_name = match.group(1)
            
            # Converte o nome da classe para minúsculas e remove o sufixo "Model"
            entity_name = class_name.lower().replace("model", "")
            
            # Adiciona o import apropriado abaixo do package
            package_declaration = f"package {main_package}.model;\n"
            import_statement_with_package = package_declaration + "\n" + import_statement
            
            # Substitui o package e adiciona o import
            java_code = java_code.replace(package_declaration, import_statement_with_package, 1)
            
            # Adiciona a anotação @Entity acima da definição da classe
            entity_annotation = f'\n@Entity(name = "{entity_name}")'
            java_code = class_pattern.sub(entity_annotation + match.group(0), java_code)
            
            # Escreve o código Java modificado de volta para o arquivo
            with open(file_path, 'w') as java_file:
                java_file.write(java_code)
