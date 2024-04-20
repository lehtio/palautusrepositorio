from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
       #  print("Tiedoston sisältö:", content)

        # Deserialisoi TOML-formaatissa oleva merkkijono
        toml_data = toml.loads(content)
        # print("Deserialisoitu data:", toml_data)

        # projektin tiedot
        poetry_info = toml_data.get("tool", {}).get("poetry", {})
        name = poetry_info.get("name", "Test name")
        description = poetry_info.get("description", "Test description")
        license = poetry_info.get("license", "-")
        authors = poetry_info.get("authors", [])

        #riippuvuudet
        dependencies = poetry_info.get("dependencies", {})
        dev_dependencies = poetry_info.get("group", {}).get("dev-dependencies", {})

        #  Project-olio 
        project = Project(name, description, dependencies, dev_dependencies)

        # lisenssit
        project.license = license
        project.authors = authors

        return project
