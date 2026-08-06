---
name: kskill-aws-cloudwatch-alarms
description: >
  Minimal CloudWatch alarms for ALVS Fargate astro-drf-aws services: target
  health, 5xx, RDS storage. Use when adding or reviewing alarms/SNS for a
  project. Keep the set tiny; no elasticache, no Lambda noise.
---

> [!warning] Ported skill — remap before trusting
> This skill came from another clone of the harness, and its body still speaks
> that clone's world: **law citations** (ADRs and docs that may not exist here —
> only `adr-00`..`adr-04` do) and **origin specifics** (cloud accounts, profiles,
> project slugs, template paths, naming schemes). None of it is in force or in
> effect here ([[adr-01-constitution]]). On adoption, remap each citation to this
> project's own ADR and each specific to this project's own values — or delete
> the skill ([[adr-02-harness]] rules 3, 5, 6).

# kskill-aws-cloudwatch-alarms

## Philosophy

`desiredCount: 1` + cost discipline → **few alarms**, high signal. Prefer SNS email to on-call for prod only.

## Alarm set (per project, per env)

| # | Name pattern | Metric | Threshold idea |
|---|--------------|--------|----------------|
| 1 | `alvs-<env>-<project>-backend-unhealthy` | TG `UnHealthyHostCount` | ≥ 1 for 2–3 periods |
| 2 | `alvs-<env>-<project>-frontend-unhealthy` | same on frontend TG | same |
| 3 | `alvs-<env>-<project>-backend-5xx` | ALB/TG `HTTPCode_Target_5XX_Count` | > N in 5 min |
| 4 | `alvs-<env>-pg-storage` (shared DB) | RDS `FreeStorageSpace` | low water mark |

Optional later: ECS CPU > 80% for 15m (right-size signal, not page).

## Naming / tags

- Alarm name prefix `alvs-<env>-`  
- Tag `App=<project>`, `Env=<env>`  
- Actions: SNS topic `alvs-<env>-alerts` (create once per env if missing)

## SNS

```bash
aws sns create-topic --name alvs-prod-alerts --region us-east-1 --profile kodex
# subscribe email — human must confirm
```

Link alarms with `AlarmActions` = topic ARN. Encrypt topic if account policy requires it.

## Do not create

- Alarms for Redis/ElastiCache  
- Dozens of per-URL synthetic canaries by default  
- Billing alarms here → `kskill-aws-cost`  
- Alarms that fire on every deploy blip (use longer evaluation periods)

## Verify

```bash
aws cloudwatch describe-alarms --alarm-name-prefix alvs- --profile kodex --region us-east-1
aws elbv2 describe-target-groups --query "TargetGroups[?contains(TargetGroupName, '<project>')].[TargetGroupName,TargetGroupArn]" --profile kodex --region us-east-1
```

## Related

`kskill-aws-observability` · `kskill-aws-troubleshoot` · `kskill-aws-cost`
