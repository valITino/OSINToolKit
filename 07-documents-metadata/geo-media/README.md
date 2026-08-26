# Geo media

You have a photo or video and want to know where it was taken. Sometimes the file
tells you outright; more often the frame does, and you have to read it.

## Check the metadata first

Run [ExifTool](../metadata-extraction/exiftool.md) before anything else - if GPS
tags survived, you are done:

```bash
exiftool -gps:all -n image.jpg      # lat/long as decimals, if present
```

Assume it is usually stripped: most social platforms remove EXIF on upload, so a
clean file is the norm, not a dead end. Absence is not evidence the photo lacks a
location - only that this copy lost it.

## Geolocate from the frame (chronogeolocation)

When metadata is gone, the image itself is the source:

- **Fixed clues**: signage, language, licence plates, architecture, road markings,
  vegetation, mountains on the horizon. Each narrows the region.
- **Reverse image search** the whole frame and distinctive crops
  ([Yandex](../../08-people-and-identity/reverse-image/yandex-images.md) is strong on
  places and buildings; [TinEye](../../08-people-and-identity/reverse-image/tineye.md)
  for exact reuse).
- **Cross-reference maps and imagery**: Google Street View, satellite view, and
  OpenStreetMap to confirm a candidate location.
- **Shadows and sun** give time-of-day and, with the date, latitude - the basis of
  chronogeolocation.

## Video and platforms

- YouTube and similar: descriptions, comments, and channel history add context;
  some third-party maps plot geotagged uploads (availability changes - verify
  before relying).
- Extract frames, then treat each as a still with the method above.

## Related

- [../metadata-extraction/exiftool.md](../metadata-extraction/exiftool.md)
- [../../08-people-and-identity/reverse-image/README.md](../../08-people-and-identity/reverse-image/README.md)
