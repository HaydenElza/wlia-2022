# WLIA 2022

This is a repository for my presentation at WLIA 2022.

[Link to slides.](https://docs.google.com/presentation/d/1Zlo_Gr2Gj5FMem08MFTJqQNMpyEP0Y-4SAreQTla9tg/edit?usp=sharing)

**PDF Maps: From Static to Interactive to “Wait, I Didn’t Know PDFs Could Do That!”**

*You’ve probably used PDF maps before and you’ve probably even heard of a GeoPDF, but did you know that PDFs can have javascript? In this talk I will explore PDF maps from the simple interactive map exported from QGIS or GDAL to a more complicated example the pushes the limits of what can be achieved in PDFs.*

## Make GeospatialPDF with GDAL and Composition File

See `gdal` directory.

Run `create_pdfs.py` to create `test.pdf`. It takes the Wisconsin state outline shapefile and writes it to pdf.

## Example PDFs

**Parcels - Downtown Madison WI:** Basic export from desktop GIS (QGIS). Explore layers, roads off by default, measure distance, explore features with data object tool.

**Tampa FD Temporal:** Fire department service calls each day in Tampa. JavaScript bookmark allows for animation of data.

**Derived Mountain Scene - Utah:** 3D animation/interface for ortho draped over LiDAR. Explore the area in 3D space and checkout the bookmarks for a vantage point.