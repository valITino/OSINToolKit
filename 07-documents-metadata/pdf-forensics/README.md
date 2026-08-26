# PDF forensics

PDF structure: objects, incremental updates, embedded images, hidden revisions.

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [binwalk](binwalk.md) | Is there another file hidden inside this one - an archive, an image, or a document | 2 | passive |
| [pdf-parser.py](pdf-parser.md) | What is actually inside this PDF at the object level - embedded files, JavaScript, | 2 | passive |
| [pdfimages](pdfimages.md) | What images are embedded in this PDF, and what metadata do **they** carry - camera, | 2 | passive |
| [qpdf](qpdf.md) | Has this PDF been edited after it was first saved - and if so, is the earlier version | 2 | passive |
<!-- END:TOOLS -->
