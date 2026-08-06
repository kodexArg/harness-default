---
name: kskill-aws-containers
description: >
  ALVS Fargate layout for this template only: two ECS services (Django 6+DRF
  backend :8000, Astro 7 SSR frontend :4321), ECR, shared ALB, Cloud Map.
  Use when creating or changing task definitions, services, ECR repos, deploys,
  or container networking for astro-drf-aws projects. Region us-east-1 only.
  Never EKS, EC2 launch type, Express Mode, App Runner, or NAT.
---

> [!warning] Inherited law — remap before trusting
> This skill was ported from another clone of the harness. Where its body cites
> an ADR or a document, that citation names the **origin project's** law, not
> this one: only `adr-00`..`adr-04` exist here, and referenced docs may not.
> Those citations are placeholders — nothing outside `docs/adrs/` in this clone
> is in force ([[adr-01-constitution]]). On adoption, remap each one to this
> project's own ADR or delete it; do not treat a dangling wikilink as a rule
> ([[adr-02-harness]] rules 3 and 6).

# kskill-aws-containers

**Only stack:** ECS **Fargate** + **ECR** for the astro-drf-aws template on **ALVS** (`789650504128`, **us-east-1**). Doctrine: `docs/INFRASTRUCTURE.md`. Precedent: **sroa** on clusters `alvs-dev` / `alvs-prod`.

## Fixed topology (do not invent alternatives)

| Item | Value |
|------|--------|
| Account | ALVS `789650504128` |
| Region | **us-east-1 only** |
| Envs | **dev**, **prod** — no staging |
| Clusters | `alvs-dev`, `alvs-prod` |
| Services | `<project>-backend`, `<project>-frontend` |
| Launch | **FARGATE**, `awsvpc`, public IP on tasks |
| Backend | port **8000**, ASGI (Django 6 + DRF) |
| Frontend | port **4321**, Astro 7 SSR, bind `0.0.0.0` |
| CPU/mem baseline | **256 / 512** (Fargate-valid). Raise only when measured (sroa backend prod is 512/1024 — exception, not default) |
| desiredCount | **1** until load proves otherwise |
| ECR | `alvs/<project>-backend`, `alvs/<project>-frontend` |
| Image tag | `<env>-<full-git-sha>` — **never** `latest` |
| ALB | shared `alvs-<env>-alb` (not one ALB per project) |
| TG | `tg-<project>-backend-<env>` :8000 · `tg-<project>-frontend-<env>` :4321 |
| Health (target) | backend `/api/health/` (API.md) · frontend document a probe (`/healthz` or `/`) |
| Logs | awslogs → `/alvs/<project>/<component>-<env>` |
| Secrets | task **secrets** from Secrets Manager only — see `kdx-aws-secrets-*` |
| SSR→API | Cloud Map `<project>-backend.<project>-<env>.local:8000` — **never** public ALB |

### Forbidden

- EKS, ECS on EC2, App Runner, ECS Express Mode, Lambda containers  
- **NAT gateways** (tasks use public IPs on purpose)  
- Private-only task subnets for app containers  
- Redis/ElastiCache sidecars  
- Mutable tags, dual-region active-active  
- Profile/region other than ALVS us-east-1 for this template  

## Fargate CPU/memory (valid pairs only)

| CPU | Memory (MiB) |
|-----|----------------|
| 256 | 512, 1024, 2048 |
| 512 | 1024–4096 (1 GiB steps) |
| 1024 | 2048–8192 |

Default for both services: **256 / 512**. Invalid pairs → reject, do not “almost” write them.

## Task definition shape

```
family: <project>-<component>-<env>     # e.g. sroa-backend-prod
networkMode: awsvpc
requiresCompatibilities: [FARGATE]
cpu / memory: strings ("256","512")
executionRoleArn: alvs-<env>-<project>-<component>-exec-role
taskRoleArn:      alvs-<env>-<project>-<component>-task-role
container:
  name: <project>-<component>
  image: 789650504128.dkr.ecr.us-east-1.amazonaws.com/alvs/<project>-<component>:<env>-<sha>
  portMappings: [{ containerPort: 8000|4321, protocol: tcp }]
  essential: true
  environment: non-secrets only (see docs/VARIABLES.md)
  secrets: JSON keys from alvs/<env>/<project>/{db,django,s3,...}
  logConfiguration: awslogs → /alvs/<project>/<component>-<env>, region us-east-1
```

- **Frontend:** zero secret refs; only `PUBLIC_*` + `PORT`/`HOST`/`BACKEND_API_URL` (Cloud Map).  
- **Backend:** inject every secret declared in `docs/VARIABLES.md` as `valueFrom` ARNs (full ARN + JSON key).

## Service shape

- Cluster `alvs-<env>`, service name `<project>-backend` | `<project>-frontend`  
- `assignPublicIp: ENABLED`, subnets = **public** (`alvs-<env>-pub-*`), SG = `alvs-<env>-task-sg`  
- Register with target group for that component  
- Service discovery: Cloud Map namespace `<project>-<env>.local`  
- Deploy: rolling, circuit breaker optional; no blue/green unless explicitly requested  

## ECR

```bash
# create once per component
aws ecr create-repository --repository-name alvs/<project>-backend --region us-east-1 --profile kodex
aws ecr create-repository --repository-name alvs/<project>-frontend --region us-east-1 --profile kodex
```

Push only via GHA OIDC (`gha-deploy-<env>`) — long-lived keys forbidden (`docs/INFRASTRUCTURE.md` CI/CD).

## ALB path ownership (shared ALB)

Host: `<project>.dev.grupoalvs.com` (dev) / `<project>.grupoalvs.com` (prod).

| Priority idea | Path / host | Target |
|---------------|-------------|--------|
| High | `/accounts/*` `/ws/*` `/api/*` `/admin/*` `/static/*` `/media/*` | backend TG |
| Host default | catch-all for project host | frontend TG |
| ALB default | unknown host | **fixed 404** |

`:80` → redirect `:443`. TLS 1.3. Do not add a second public ALB per project.

## Read-only survey commands (profile `kodex`, region `us-east-1`)

```bash
aws ecs list-services --cluster alvs-prod --profile kodex --region us-east-1
aws ecs describe-services --cluster alvs-prod --services <project>-backend --profile kodex --region us-east-1
aws ecs describe-task-definition --task-definition <family> --profile kodex --region us-east-1
aws ecr describe-repositories --repository-names alvs/<project>-backend --profile kodex --region us-east-1
```

## Related skills

`kskill-aws-iam` · `kskill-aws-secrets-manager` · `kskill-aws-observability` · `kskill-aws-troubleshoot` · app: `kskill-django-6-drf` · `kskill-astro-7`
