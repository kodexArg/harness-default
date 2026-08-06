---
name: kskill-aws-cost
description: >
  Cost discipline for ALVS astro-drf-aws: Fargate 256/512, no NAT, no Redis,
  shared ALB, single-AZ micro RDS. Use when reviewing spend, rightsizing, or
  blocking expensive “best practice” additions. Account 789650504128 us-east-1.
---

> [!warning] Ported skill — remap before trusting
> This skill came from another clone of the harness, and its body still speaks
> that clone's world: **law citations** (ADRs and docs that may not exist here —
> only `adr-00`..`adr-04` do) and **origin specifics** (cloud accounts, profiles,
> project slugs, template paths, naming schemes). None of it is in force or in
> effect here ([[adr-01-constitution]]). On adoption, remap each citation to this
> project's own ADR and each specific to this project's own values — or delete
> the skill ([[adr-02-harness]] rules 3, 5, 6).

# kskill-aws-cost

## Non-negotiable cost opinions (template)

| Decision | Why |
|----------|-----|
| **No NAT Gateway** | Tasks use public IPs — deliberate (`docs/INFRASTRUCTURE.md`) |
| **No Redis / ElastiCache** | `DatabaseCache` only (`docs/CACHE.md`) |
| **Shared ALB** per env | Not one ALB per project |
| **Fargate 256 CPU / 512 MB** baseline | Scale only when measured |
| **desiredCount: 1** | Until load proves otherwise |
| **RDS `db.t4g.micro` single-AZ** | `alvs-*-pg` precedent |
| **dev + prod only** | No staging tier |
| **Log retention short** | 14–30 days default |

Any proposal that adds NAT, Redis, Multi-AZ RDS “because production”, or second ALB must be **rejected** unless the user overrides in-turn with explicit justification.

## When the agent must refuse

- “Move tasks to private subnets + NAT for security”  
- “Add ElastiCache for Django cache”  
- “Multi-AZ RDS for the template default”  
- “Fargate 2 vCPU because why not”  
- “Always-on NAT for ECR pulls” (use public IP + ECR endpoints optional later)

## Allowed cost work

- Cost Explorer by service/tag for account `789650504128`  
- Right-size **after** CloudWatch CPU/mem evidence (`kskill-aws-observability`)  
- Budgets/alerts for unexpected spend  
- ECR lifecycle policies to expire untagged images  
- Spot **not** for this SSR pair (stick to Fargate standard)

## Math rule

Never freehand arithmetic on cost figures — use a short Python script or CLI output.

## Date rule

Before Cost Explorer queries, use the **real current date** (today’s year is not training data).

## Related

`kskill-aws-containers` · `kskill-aws-observability` · `docs/INFRASTRUCTURE.md` · `docs/CACHE.md`
