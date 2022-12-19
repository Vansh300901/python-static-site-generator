import typer
import Site from ssg.site

def main(source = "content", dest = "dist"):
    config = {
        "source" : source,
        "dest" : dest
    }

    SiteInstance = Site(config["source"], config["dest"])
    SiteInstance.build()

typer.run(main())

