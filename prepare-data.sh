#!/bin/bash

mkdir VESSEL12_01-20_Lungmasks  && \
mkdir VESSEL12_ExampleScans  && \
tar -xvf VESSEL12_01-20_Lungmasks.tar.bz2 -C VESSEL12_01-20_Lungmasks  && \
unzip exampleScans.zip && \
tar -xvf VESSEL12_ExampleScans.tar.bz2 -C VESSEL12_ExampleScans && \
tar -xvf VESSEL12_01.tar.bz2 && \
tar -xvf VESSEL12_02.tar.bz2 && \
tar -xvf VESSEL12_03.tar.bz2 && \
tar -xvf VESSEL12_04.tar.bz2 && \
tar -xvf VESSEL12_05.tar.bz2 && \
mv *.mhd VESSEL12_01-05 && \
mv *.raw VESSEL12_01-05 && \
rm VESSEL12_01.tar.bz2 VESSEL12_02.tar.bz2 VESSEL12_03.tar.bz2 VESSEL12_04.tar.bz2 VESSEL12_05.tar.bz2 && \
tar -xvf VESSEL12_06.tar.bz2 && \
tar -xvf VESSEL12_07.tar.bz2 && \
tar -xvf VESSEL12_08.tar.bz2 && \
tar -xvf VESSEL12_09.tar.bz2 && \
tar -xvf VESSEL12_10.tar.bz2 && \
mv *.mhd VESSEL12_06-10 && \
mv *.raw VESSEL12_06-10 && \
rm VESSEL12_06.tar.bz2 VESSEL12_07.tar.bz2 VESSEL12_08.tar.bz2 VESSEL12_09.tar.bz2 VESSEL12_10.tar.bz2 && \
tar -xvf VESSEL12_11.tar.bz2 && \
tar -xvf VESSEL12_12.tar.bz2 && \
tar -xvf VESSEL12_13.tar.bz2 && \
tar -xvf VESSEL12_14.tar.bz2 && \
tar -xvf VESSEL12_15.tar.bz2 && \
mv *.mhd VESSEL12_11-15 && \
mv *.raw VESSEL12_11-15 && \
rm VESSEL12_11.tar.bz2 VESSEL12_12.tar.bz2 VESSEL12_13.tar.bz2 VESSEL12_14.tar.bz2 VESSEL12_15.tar.bz2 && \
tar -xvf VESSEL12_16.tar.bz2 && \
tar -xvf VESSEL12_17.tar.bz2 && \
tar -xvf VESSEL12_18.tar.bz2 && \
tar -xvf VESSEL12_19.tar.bz2 && \
tar -xvf VESSEL12_20.tar.bz2 && \
mv *.mhd VESSEL12_16-20 && \
mv *.raw VESSEL12_16-20 && \
rm VESSEL12_16.tar.bz2 VESSEL12_17.tar.bz2 VESSEL12_18.tar.bz2 VESSEL12_19.tar.bz2 VESSEL12_20.tar.bz2