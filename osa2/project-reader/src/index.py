from project_reader import ProjectReader

def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml"
    reader = ProjectReader(url)
    project = reader.get_project()

    print("Name:", project.name)
    print("Description:", project.description)
    print("License:", project.license)

    print("\nAuthors:")
    for author in project.authors:
        print("-", author)

    print("\nDependencies:")
    for dependency in project.dependencies:
        print("-", dependency)

    print("\nDevelopment dependencies:")
    for dev_dependency in project.dev_dependencies:
        print("-", dev_dependency)

if __name__ == "__main__":
    main()
