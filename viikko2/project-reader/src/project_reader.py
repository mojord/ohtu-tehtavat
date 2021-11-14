from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed = toml.loads(content)

        deplist = []
        devlist = []

        toollist  = parsed.get("tool")
        poetrylist = toollist.get("poetry")
        name = poetrylist.get("name")
        description = poetrylist.get("description")
        for dep in poetrylist.get("dependencies"):
            deplist.append(dep)
        for dev in poetrylist.get("dev-dependencies"):
            devlist.append(dev)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, deplist, devlist)
