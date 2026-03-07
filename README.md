Python (Foundation of everything)
Current level    →  if/else, dictionaries, tuples
Need to reach    →  functions, OOP basics, error handling,
                    pandas, requests, boto3, FastAPI
Timeline         →  2–3 months daily practice
Linux (You likely have basics from KodeKloud)
Need             →  file permissions, process management,
                    environment variables, bash scripting basics,
                    curl, systemd, navigating logs
Why              →  debugging inside Docker containers and EC2
Docker
Need             →  write Dockerfiles, build/push images,
                    docker-compose for local testing,
                    understand layers and image optimization
Why              →  containerizing the FastAPI app
AWS Core
Need             →  IAM (roles, policies — critical),
                    S3 (buckets, permissions, boto3),
                    ECR (pushing Docker images),
                    EKS (managed Kubernetes),
                    CloudWatch (logs, alarms, dashboards)
Why              →  entire project runs on AWS
Certification    →  AWS SAA validates all of this
Terraform
Need             →  resources, variables, outputs, modules,
                    remote state (S3 + DynamoDB),
                    terraform init/plan/apply/destroy
Why              →  provisioning EKS, S3, ECR, CloudWatch
You already have →  some exposure, go deeper now
Kubernetes
Need             →  Deployments, Services, Ingress,
                    ConfigMaps, resource limits,
                    kubectl commands, health probes,
                    namespace management
Why              →  running the API on EKS
You already love →  this, so it'll feel natural
Certification    →  CKA solidifies this
ML Basics (just enough, not deep)
Need             →  pandas (data manipulation),
                    scikit-learn (train/evaluate model),
                    MLflow (track experiments),
                    joblib (save/load model),
                    basic metrics (accuracy, precision, recall)
Why              →  building the prediction model
NOT needed       →  deep learning, neural networks,
                    math/statistics at deep level
FastAPI
Need             →  creating endpoints (GET, POST),
                    Pydantic models for validation,
                    running with uvicorn,
                    basic error handling
Why              →  exposing the ML model as an API
Learn time       →  1–2 weeks, very beginner friendly
Git + GitHub
Need             →  branching, commits, pull requests,
                    writing good READMEs (Markdown),
                    GitHub Actions basics (optional but good)
Why              →  your entire portfolio lives here
You have         →  account already, just need daily commits

Honest skill priority order for you:
Priority 1  →  Python (boto3, pandas, FastAPI)
               Nothing works without this

Priority 2  →  AWS + Terraform
               Your infra foundation

Priority 3  →  Docker
               Bridge between code and K8s

Priority 4  →  Kubernetes deeper (EKS specific)
               You already love this

Priority 5  →  ML basics (scikit-learn + MLflow)
               Smallest learning curve in the project

Priority 6  →  FastAPI
               Quickest to learn, very satisfying
