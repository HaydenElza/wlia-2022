# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# create_pdfs.py
# Create PDFs using gdal composition file.
# Hayden Elza (hayden.elza@gmail.com)
# Created: 2022-02-24
# Modified: 
#------------------------------------------------------------------------------

import os
from osgeo import gdal


# Define variables
composition_file = 'composition.xml'
output_file = 'test.pdf'

# Bounds of page in geo space
xmin = 294838.9998751305975020
xmax = 770036.3720441744662821
ymin = 225108.8125283487315755
ymax = 734398.4375955514842644

# Composition file
xml_content = """
    <PDFComposition>
        <Metadata>
            <Author>Anonymous</Author>
        </Metadata>

        <LayerTree displayOnlyOnVisiblePages="true">
            <Layer id="l1" name="State"/>
        </LayerTree>

        <Page id="page_1">
            <DPI>72</DPI>
            <Width>612</Width>
            <Height>792</Height>

            <Georeferencing id="georeferenced">
                <SRS dataAxisToSRSAxisMapping="2,1">EPSG:3071</SRS>
                <BoundingBox x1="1" y1="1" x2="612" y2="792"/>
                <BoundingPolygon>POLYGON(({ymin} {xmin},{ymax} {xmin},{ymax} {xmax},{ymin} {xmax},{ymin} {xmin}))</BoundingPolygon>
                <ControlPoint x="1"  y="1"  GeoY="{ymin}"  GeoX="{xmin}"/>
                <ControlPoint x="1"  y="792" GeoY="{ymax}"  GeoX="{xmin}"/>
                <ControlPoint x="612"  y="1"  GeoY="{ymin}"  GeoX="{xmax}"/>
                <ControlPoint x="612"  y="792" GeoY="{ymax}"  GeoX="{xmax}"/>
            </Georeferencing>

            <Content>
                <IfLayerOn layerId="l1">
                    <Vector dataset="data/Wisconsin_State_Boundary_24K.shp" layer="Wisconsin_State_Boundary_24K" georeferencingId="georeferenced">
                    </Vector>
                </IfLayerOn>
            </Content>
        </Page>

    </PDFComposition>
    """.format(xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)

# Write xml to file
with open(composition_file, 'w') as f:
    f.write(xml_content)

# Write PDF
gdal.GetDriverByName("PDF").Create(
    output_file, 0, 0, 0, gdal.GDT_Unknown,
    options = ['COMPOSITION_FILE=' + composition_file])

# Remove xml
os.remove(composition_file)
