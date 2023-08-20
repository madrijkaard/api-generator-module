import os
import json
from pathlib import Path

def create_directories(path):
    try:
        os.makedirs(path)
        print(f"Created directory: {path}")
    except FileExistsError:
        print(f"Directory already exists: {path}")

def create_pom_xml(project_directory, pom_template_path, spring_boot_starter_parent_version, group_id, artifact_id, project_name, java_version):
    with open(pom_template_path, "r") as template_file:
        pom_template = template_file.read()

    pom_content = pom_template.replace(
        "{spring_boot_starter_parent_version}", spring_boot_starter_parent_version
    ).replace(
        "{group_id}", group_id
    ).replace(
        "{artifact_id}", artifact_id
    ).replace(
        "{project_name}", project_name
    ).replace(
        "{java_version}", str(java_version)
    )

    pom_path = os.path.join(project_directory, "pom.xml")

    with open(pom_path, "w") as pom_file:
        pom_file.write(pom_content)
        print("Created pom.xml")

def create_java_file(package_path, class_name, main_package):
    java_template = """\
package {main_package};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {class_name} {{
    public static void main(String[] args) {{
        SpringApplication.run({class_name}.class, args);
    }}
}}
"""
    
    package_name = ".".join(package_path.split(os.path.sep))
    java_content = java_template.format(package_name=package_name, class_name=class_name, main_package=main_package)
    java_path = os.path.join(package_path, f"{class_name}.java")

    with open(java_path, "w") as java_file:
        java_file.write(java_content)
        print(f"Created {class_name}.java")

def create_application_properties(directory):
    application_properties_content = ""

    properties_path = os.path.join(directory, "application.properties")

    with open(properties_path, "w") as properties_file:
        properties_file.write(application_properties_content)
        print(f"Created application.properties in {directory}")

def main():
    root_directory = os.getcwd()
    config_directory = os.path.join(root_directory, "config")
    out_directory = os.path.join(root_directory, "out")

    config_path = os.path.join(config_directory, "main.json")
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
        spring_boot_starter_parent_version = config_data["spring-boot-starter-parent-version"]
        group_id = config_data["group-id"]
        artifact_id = config_data["artifact-id"]
        project_name = config_data["project-name"]
        main_package = config_data["main-package"]
        java_version = config_data["java-version"]

    pom_template_path = os.path.join(config_directory, "maven", "main.xml")

    project_directory = os.path.join(out_directory, project_name)
    create_directories(project_directory)

    for dir_name in ["src/main/java", "src/main/resources", "src/test/java", "src/test/resources"]:
        create_directories(os.path.join(project_directory, dir_name))

    main_java_path = os.path.join(project_directory, "src/main/java")
    test_java_path = os.path.join(project_directory, "src/test/java")

    for package_name in main_package.split("."):
        main_java_path = os.path.join(main_java_path, package_name)
        test_java_path = os.path.join(test_java_path, package_name)
        create_directories(main_java_path)
        create_directories(test_java_path)

    create_pom_xml(
        project_directory,
        pom_template_path,
        spring_boot_starter_parent_version,
        group_id,
        artifact_id,
        project_name,
        java_version
    )

    artifact_camel_case = "".join(word.capitalize() for word in artifact_id.split("-"))
    class_name = f"{artifact_camel_case}Application"
    create_java_file(main_java_path, class_name, main_package)

    create_application_properties(os.path.join(project_directory, "src/main/resources"))
    create_application_properties(os.path.join(project_directory, "src/test/resources"))

if __name__ == "__main__":
    main()
