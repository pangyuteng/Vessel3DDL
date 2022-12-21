
+ build container.
```
docker build -t vessel3ddl docker
```

+ specify variable `VESSEL12_DIR` and head into container.
```
export VESSEL12_DIR=xxx
docker run -it -w /workdir -v $PWD:/workdir \
    -v $VESSEL12_DIR:/workdir/Data/VESSEL12 vessel3ddl bash
```

+ optional - format data per `../README.md`
```
bash prepare-data.sh
```

+ train classifier per `../README.md`
```
bash run.sh
```
