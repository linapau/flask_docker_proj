# Helm chart for flaskDocker

This chart deploys the Flask application and a MySQL database to Kubernetes.

## Image placeholder

Set the container image in values.yaml before installing:

```yaml
image:
  repository: your-registry/your-image
  tag: latest
```

## Install

```bash
helm install flaskdocker ./helm
```

## Upgrade

```bash
helm upgrade --install flaskdocker ./helm
```
