
```
docker build -t vessel3ddl docker
export DATADIR=??
ln -s /scratch2/personal/pteng/dataset/VESSEL12 $DATADIR

docker run -it -w /workdir -v $PWD:/workdir vessel3ddl bash

cd scripts/LearnDictionary/
python ExtractPatches.py

```
