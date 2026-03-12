# pandoc_writing_template

quick and dirty template for my writing projects done in pandoc markdown

## Usage: 

1. Create a new repository with this one as a template (or just copy it). 

2.  Edit the values of `names.json` with the appropriate values for document title, project title, citation file title that you'll be using (I use CSL json files generated and auto-updated by Zotero with Better Bibtex), preferred citation format, and, if you're not me, author name. :-)  

3. Run `./buildstub` (you may need to use `chomd + x` to make it executable), a shell script which will leave you with the following files: 

- `draft.md`: the markdown file to write the draft in.

- `quickbuild`: a shell script to, as the name suggests, quickly build the document in word and PDF formats, and also do a git commit.  The build will, I suspect, throw an error if there isn't a citation file.  Also, you might need to use `chomd + x` to make this one executable too.

- `cleanup.py` a helper python script to get rid of useless fields from the citation files, so that we don't end up with academic articles with URLS in addition to their citations etc. 

Everything else will be moved to the directory `repository_template_files`, which contains the templating files necessary to build the stub.  After building it may safely be ignored or deleted. 

In addition, this repository contains `pandoc_dependencies` which has, as the name suggests, the dependencies that the pandoc build process I use requires, and `alternative_date_system` which has an additional python script (and slightly tweaked `quickbuild`) that I used to use to update the dates on each build before I realized that pandoc has a built-in lua script these days to do that.