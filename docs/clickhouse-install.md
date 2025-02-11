# Install Clickhouse via Helm

[Clickhouse Operator](https://blog.duyet.net/2024/03/clickhouse-on-kubernetes.html)

tldr:

```sh
helm repo add clickhouse-operator https://docs.altinity.com/clickhouse-operator
```

```sh
helm upgrade --install --create-namespace --namespace my-iot clickhouse-operator clickhouse-operator/altinity-clickhouse-operator
```

```sh
kubectl get pods -n my-iot
```

Deploy first single node clickhouse

[clickhouse-single.yaml](/k8s/clickhouse-single.yaml)

```sh
kubectl apply -f clickhouse-single.yaml -n my-iot
```

```sh
kubectl get po -n my-iot 
```

```sh
kubectl get svc -n my-iot
```

Post-forward playground

```sh
kubectl port-forward svc/clickhouse-single 8123 -n my-iot
```

Go to [http://localhost:8123/play](http://localhost:8123/play)

![playground clickhouse](/images/01.png)

Built-in dashboard

Go to [http://localhost:8123/dashboard](http://localhost:8123/dashboard)