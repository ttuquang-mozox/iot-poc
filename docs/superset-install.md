# Install Apache Superset via Helm

```sh
helm repo add superset https://apache.github.io/superset
```

Create `values.yaml` from [values.yaml](https://github.com/apache/superset/tree/master/helm/superset/values.yaml) and override

1. Generate key via shell

```sh
openssl rand -base64 42
```

Override `values.yaml`
```yaml
configOverrides:
  secret: |
    SECRET_KEY = 'YOUR_OWN_RANDOM_GENERATED_SECRET_KEY'
```

2. [ModuleNotFoundError: No module named 'psycopg2' during k8 installation #31431](https://github.com/apache/superset/discussions/31431)

Override `values.yaml` 
```yaml
bootstrapScript: |
  #!/bin/bash
  
  # Install system-level dependencies
  apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

  # Install required Python packages
  pip install \
    authlib \
    psycopg2-binary \
    mysqlclient \

  # Create bootstrap file if it doesn't exist
  if [ ! -f ~/bootstrap ]; then
    echo "Running Superset with uid {{ .Values.runAsUser }}" > ~/bootstrap
  fi
```

```sh
helm upgrade --install --values superset-values.yaml superset superset/superset
```

