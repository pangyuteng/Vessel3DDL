
```
docker build -t vessel3ddl docker
export VESSEL12_DIR=xxx
docker run -it -w /workdir -v $PWD:/workdir \
    -v $VESSEL12_DIR:/workdir/Data/VESSEL12 vessel3ddl bash

Follow README.md to train classifier

cd /workdir/scripts/LearnDictionary
python ExtractPatches.py
python LearnDictionary.py

cd /workdir/scripts/LearnClassifier
python ExtractXy_multithread.py
python ConcatenateXy.py
python TrainClassifier.py

cd /workdir/scripts/UseClassifier
python UseClassifier.py
```
