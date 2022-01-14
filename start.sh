#!/bin/bash
k3d cluster create kafka-umbrella
### installing argocd
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
#### applying application yaml
kubectl apply -f argocd/dev/application.yaml
