# Install Grafana

```sh
kubectl apply -f grafana.yaml
```

```sh
kubectl port-forward service/grafana 3000:3000 --namespace=my-iot
```
