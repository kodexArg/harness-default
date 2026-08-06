---
name: kskill-aws-cloudwatch-query
description: >
  CloudWatch Logs Insights queries for ALVS Fargate Django and Astro services.
  Use when searching app logs, 5xx, tracebacks, or deploy windows. Log groups
  /alvs/<project>/* only. Not Athena/S3 Tables export skills.
---

> [!warning] Ported skill — remap before trusting
> This skill came from another clone of the harness, and its body still speaks
> that clone's world: **law citations** (ADRs and docs that may not exist here —
> only `adr-00`..`adr-04` do) and **origin specifics** (cloud accounts, profiles,
> project slugs, template paths, naming schemes). None of it is in force or in
> effect here ([[adr-01-constitution]]). On adoption, remap each citation to this
> project's own ADR and each specific to this project's own values — or delete
> the skill ([[adr-02-harness]] rules 3, 5, 6).

# kskill-aws-cloudwatch-query

**This skill is Logs Insights for our Fargate apps** — not CloudWatch “system tables” / Iceberg SQL.

## Groups

```
/alvs/<project>/backend-<env>
/alvs/<project>/frontend-<env>
```

Region: **us-east-1**. Profile: **kodex**.

## Run a query

```bash
aws logs start-query \
  --log-group-name "/alvs/<project>/backend-prod" \
  --start-time $(date -d '1 hour ago' +%s) \
  --end-time $(date +%s) \
  --query-string 'fields @timestamp, @message | filter @message like /ERROR|Traceback|5[0-9]{2}/ | sort @timestamp desc | limit 50' \
  --profile kodex --region us-east-1

aws logs get-query-results --query-id <id> --profile kodex --region us-east-1
```

## Query pack (copy/adapt)

### Recent errors (Django)

```
fields @timestamp, @message
| filter @message like /ERROR|CRITICAL|Traceback|Exception/
| sort @timestamp desc
| limit 100
```

### HTTP 5xx / 4xx if access log lines exist

```
fields @timestamp, @message
| filter @message like / 5[0-9][0-9] | 4[0-9][0-9] /
| sort @timestamp desc
| limit 100
```

### Secret / settings boot failures

```
fields @timestamp, @message
| filter @message like /ImproperlyConfigured|SECRET_KEY|DatabaseError|could not connect/
| sort @timestamp desc
| limit 50
```

### Frontend SSR upstream (Cloud Map backend)

```
fields @timestamp, @message
| filter @message like /ECONNREFUSED|fetch failed|backend|8000|ETIMEDOUT/
| sort @timestamp desc
| limit 50
```

### Count errors per 5 minutes

```
stats count(*) as n by bin(5m)
| filter @message like /ERROR|Traceback/
```

## Rules

- Default window: last **1h**; widen only if needed (cost + noise).  
- Prefer one component log group per query.  
- **Never** paste log lines that contain secrets; redact.  
- If group missing: check task def `awslogs-group` (`kskill-aws-observability`).  

## Related

`kskill-aws-observability` · `kskill-aws-troubleshoot`
