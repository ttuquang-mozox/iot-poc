# PoC Durian

## Pulsar Docker
```sh
docker run -it \
-p 6650:6650 \
-p 8080:8080 \
--mount source=pulsardata,target=/pulsar/data \
--mount source=pulsarconf,target=/pulsar/conf \
apachepulsar/pulsar:4.0.2 \
bin/pulsar standalone
```

```sh
mkdir -p pulsardata pulsarconf
```
