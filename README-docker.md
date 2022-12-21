
```
docker build -t vessel3ddl docker
export VESSEL12_DIR=xxx
docker run -it -w /workdir -v $PWD:/workdir \
    -v $VESSEL12_DIR:/workdir/Data/VESSEL12 vessel3ddl bash

cd scripts/LearnDictionary/
python ExtractPatches.py

```
