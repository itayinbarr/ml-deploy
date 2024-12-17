# ML Model Deployment Template

I wrote this repository to myself as a template for deploying a custom PyTorch model using a Flask backend, complete with:

- Local development environment using Docker Compose
- Kubernetes manifests for production deployment
- Terraform scripts for infrastructure provisioning
- CI/CD pipelines via GitHub Actions
- Autoscaling with Horizontal Pod Autoscaler (HPA)
- Monitoring using Prometheus & Grafana
- Logging configuration

#### Important Note

This repository isn't working out of the box, as it is a mere template and for actual usage, specific environment variables and configurations are needed.

## Features

- **Local Development**: Spin up the service locally using `docker-compose`.
- **CI/CD**: GitHub Actions workflows for testing and deploying the application.
- **Cloud-Native**: Kubernetes manifests for scaling and updating your application.
- **Infrastructure as Code**: Terraform configuration to provision cloud resources.
- **Monitoring & Logging**: Prometheus for metrics, Grafana for visualization, and a logging config for structured logging.

## Prerequisites

- Docker & Docker Compose
- Python 3.9+ (optional if you want to run tests outside containers)
- Make (optional)
- Terraform (if you are provisioning infrastructure)
- kubectl & a Kubernetes cluster (for production deployment)

## Local Development

1. **Clone the Repo**:

   ```bash
   git clone https://github.com/itayinbarr/ml-deploy.git
   cd ml-deployment
   ```

2. **Install Dependencies (Optional)**:

   ```bash
   pip install -r src/requirements.txt
   ```

3. **Run Tests**:

   ```bash
   make test
   ```

4. **Run Locally**:

   ```bash
   make run-local
   ```

   This will start the Flask app at `http://localhost:5000`, Prometheus at `http://localhost:9090`, and Grafana at `http://localhost:3000`.

5. **Test the Predict Endpoint**:

   ```bash
   curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"input": [1,2,3]}'
   ```

## Production Deployment

1. **Provision Infrastructure**: Use Terraform in `infra/terraform` to provision a Kubernetes cluster and related resources:

   ```bash
   cd infra/terraform
   terraform init
   terraform apply
   ```

2. **Build and Push Image** (automated via GitHub Actions on `main` push, or manually):

   ```bash
   docker build -t <registry-url>/<repo>:latest .
   docker push <registry-url>/<repo>:latest
   ```

3. **Deploy to Kubernetes**:

   ```bash
   kubectl apply -f infra/k8s/
   ```

4. **Access the Application**: Depending on your ingress setup:

   ```bash
   curl -X POST http://yourapp.example.com/predict \
     -H "Content-Type: application/json" \
     -d '{"input": [1,2,3]}'
   ```

## Monitoring & Logging

- **Metrics**: Visit Prometheus (for dev environment `http://localhost:9090`) or your production endpoint.
- **Dashboards**: Grafana dashboards can be configured by importing `model_performance.json` in the `infra/k8s/prometheus-grafana/dashboards` directory.
- **Logging**: Logs are printed to stdout and can be collected by a logging driver or stack of your choice.

## Scaling

The included `hpa.yaml` sets up a Horizontal Pod Autoscaler to scale the number of replicas based on CPU utilization or other metrics if configured with Prometheus Adapter.

```

```
