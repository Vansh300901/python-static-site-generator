import typer
from ssg.site import Site

def main(source = "content", dest = "dist"):
    config = {
        "source" : source,
        "dest" : dest
    }

    SiteInstance = Site(config["source"], config["dest"])
    SiteInstance.build()

typer.run(main())

