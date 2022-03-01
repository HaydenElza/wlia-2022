# PDF Maps: From Static to Interactive to “Wait, I Didn’t Know PDFs Could Do That!”

This is a repository for my presentation at WLIA 2022.

[Link to slides.](https://docs.google.com/presentation/d/1Zlo_Gr2Gj5FMem08MFTJqQNMpyEP0Y-4SAreQTla9tg/edit?usp=sharing)

**PDF Maps: From Static to Interactive to “Wait, I Didn’t Know PDFs Could Do That!”**

*You’ve probably used PDF maps before and you’ve probably even heard of a GeoPDF, but did you know that PDFs can have javascript? In this talk I will explore PDF maps from the simple interactive map exported from QGIS or GDAL to a more complicated example the pushes the limits of what can be achieved in PDFs.*

[![image](https://user-images.githubusercontent.com/10215346/155614799-0ba33d67-1743-40a8-8c65-e4084af0cea8.png)](https://docs.google.com/presentation/d/1Zlo_Gr2Gj5FMem08MFTJqQNMpyEP0Y-4SAreQTla9tg/edit?usp=sharing)

## Make GeospatialPDF with GDAL and Composition File

See `gdal` directory.

Run `create_pdfs.py` to create `test.pdf`. It takes the Wisconsin state outline shapefile and writes it to pdf.

## Example PDFs

1. **Parcels - Downtown Madison WI:** Basic export from desktop GIS (QGIS). Explore layers, roads off by default, measure distance, explore features with data object tool.
See `example_pdfs/parcels - madsion` for QGIS map files to see how random color palette symbology is done.

2. **Tampa FD Temporal:** Fire department service calls each day in Tampa. JavaScript bookmark allows for animation of data.

3. **Derived Mountain Scene - Utah:** 3D animation/interface for ortho draped over LiDAR. Explore the area in 3D space and checkout the bookmarks for a vantage point.
