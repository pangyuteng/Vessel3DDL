
# build container for training

+ build container.
```
cd .. # go to code repo root 
docker build -t vessel3ddl:train docker
```

+ mount the volume containing VESSEL12 data and head into container.
```
# DATA_DIR contains folder `VESSEL12`
export DATA_DIR=xxx
docker run -it -w /workdir -v $PWD:/workdir \
    -v $DATA_DIR:/workdir/Data vessel3ddl:train bash
```

+ optional - format data per `../README.md`
```
bash prepare-data.sh
```

+ train classifier per `../README.md`
```
cd .. # go to code repo root 
bash docker/run.sh
```

# build container for inference

+ ensure `Data/Serialized` is present in code repo root
```
cd .. # go to code repo root
cp -R ${DATA_DIR}/Serialized Data
mkdir -p Data/VESSEL12/VESSEL12_ExampleScans/Annotations
cp ${DATA_DIR}/VESSEL12/VESSEL12_ExampleScans/Annotations/*.csv Data/VESSEL12/VESSEL12_ExampleScans/Annotations
```

+ build container for inference
```
cd .. # go to code repo root
docker build -t vessel3ddl:inference -f docker/Dockerfile.inference .
```

# inference

+ head into container and mount image location as volume (for example `/mnt`)
```

docker run -it -u $(id -u):$(id -g) -v /mnt:/mnt \
    vessel3ddl:inference bash

cd /workdir/scripts/UseClassifier

python3 UseClassifier.py $input_file $output_file

```