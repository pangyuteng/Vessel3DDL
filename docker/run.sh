#!/bin/bash

cd /workdir/scripts/LearnDictionary
python ExtractPatches.py
python LearnDictionary.py

cd /workdir/scripts/LearnClassifier
python ExtractXy_multithread.py
python ConcatenateXy.py
python TrainClassifier.py

cd /workdir/scripts/UseClassifier
python UseClassifier.py
