# Kubernetes Command Note

```sh
kubectl get all -n my-iot
```

## External Access

### Method 1: Minikube Tunnel

```sh
minikube tunnel
```

### Method 2: Use Port Forwarding

```sh
kubectl port-forward svc/pulsar-service 6650:6650
```