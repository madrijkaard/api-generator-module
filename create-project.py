import os
import json
from pathlib import Path

def create_directories(path):
    try:
        os.makedirs(path)
        print(f"Created directory: {path}")
    except FileExistsError:
        print(f"Directory already exists: {path}")

def create_pom_xml(project_directory, group_id, artifact_id):
    pom_template = """\
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
         
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
        <relativePath/>
    </parent>
    
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>{group_id}</groupId>
    <artifactId>{artifact_id}</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    
    <dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-validation</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-cassandra</artifactId>
		</dependency>

		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
    </dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>
    
</project>
"""

    pom_content = pom_template.format(group_id=group_id, artifact_id=artifact_id)
    pom_path = os.path.join(project_directory, "pom.xml")

    with open(pom_path, "w") as pom_file:
        pom_file.write(pom_content)
        print("Created pom.xml")

def main():
    root_directory = os.getcwd()
    config_directory = os.path.join(root_directory, "config")
    out_directory = os.path.join(root_directory, "out")

    # Ler o arquivo main.json no diretório config
    config_path = os.path.join(config_directory, "main.json")
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
        project_name = config_data["project-name"]
        main_package = config_data["main-package"]
        group_id = config_data["group-id"]
        artifact_id = config_data["artifact-id"]

    # Criar o diretório com o mesmo nome do project-name no diretório out
    project_directory = os.path.join(out_directory, project_name)
    create_directories(project_directory)

    # Criar a sequência de diretórios em project_directory
    for dir_name in ["src/main/java", "src/main/resources", "src/test/java", "src/test/resources"]:
        create_directories(os.path.join(project_directory, dir_name))

    # Criar a estrutura de pacotes em src/main/java e src/test/java
    main_java_path = os.path.join(project_directory, "src/main/java")
    test_java_path = os.path.join(project_directory, "src/test/java")

    for package_name in main_package.split("."):
        main_java_path = os.path.join(main_java_path, package_name)
        test_java_path = os.path.join(test_java_path, package_name)
        create_directories(main_java_path)
        create_directories(test_java_path)

    # Criar o arquivo pom.xml dentro do diretório do projeto
    create_pom_xml(project_directory, group_id, artifact_id)

if __name__ == "__main__":
    main()
