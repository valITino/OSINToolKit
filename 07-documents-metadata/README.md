# 07 - Documents and Metadata

You have a file. Pull its metadata, harvest an org's public documents, and dig into PDF and Office internals for authors, revisions, and hidden content.

## Subcategories

- [metadata-extraction/](metadata-extraction/) - ExifTool, mat2 - read (and strip) metadata
- [harvest-from-web/](harvest-from-web/) - metagoofil, FOCA - collect public docs then extract
- [pdf-forensics/](pdf-forensics/) - pdf-parser.py, qpdf, pdfimages, binwalk - PDF internals
- [office-forensics/](office-forensics/) - oletools - legacy Office and macro internals
- [geo-media/](geo-media/) - Geolocating photos and video

## Tools in this category

<!-- BEGIN:TOOLS -->
| Tool | Answers | Tier | Contact |
|---|---|---|---|
| [ExifTool](metadata-extraction/exiftool.md) | I have a file - a photo, a PDF, a Word doc, almost anything. What metadata is | 1 | passive |
| [binwalk](pdf-forensics/binwalk.md) | Is there another file hidden inside this one - an archive, an image, or a document | 2 | passive |
| [mat2](metadata-extraction/mat2.md) | I am about to publish or hand over a file. What metadata would leak with it, and how | 2 | passive |
| [oletools](office-forensics/oletools.md) | What is inside this Office document - who authored it, what macros does it carry, and | 2 | passive |
| [pdf-parser.py](pdf-forensics/pdf-parser.md) | What is actually inside this PDF at the object level - embedded files, JavaScript, | 2 | passive |
| [pdfimages](pdf-forensics/pdfimages.md) | What images are embedded in this PDF, and what metadata do **they** carry - camera, | 2 | passive |
| [qpdf](pdf-forensics/qpdf.md) | Has this PDF been edited after it was first saved - and if so, is the earlier version | 2 | passive |
| [FOCA](harvest-from-web/foca.md) | What documents has this organisation published, and what does their metadata reveal | 3 | passive |
| [metagoofil](harvest-from-web/metagoofil.md) | What documents has this organisation published, and what usernames, software, and | 3 | passive |
<!-- END:TOOLS -->
