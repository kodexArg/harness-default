---
title: API
description: API surface — endpoints, contracts, auth, and versioning
version: v0.1.0
updated: 2026-08-06
---

# API

This file is the **only** source of valid endpoints. An endpoint is valid if
and only if it has a row below. A route that exists in `urls.py` but not here
does not exist — `khook-check-api` reads this file and refuses the route until
its row is added first.

## Endpoints

The row shape below is machine-read: `| METHOD | \`/path/\` | …`. Keep the
method bare (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`, `WS`)
and the path in backticks, leading slash included. Path parameters are written
`<id>`; the hook treats them as skippable filler when matching a route's
literal segments.

| Method | Path | Auth | Request | Response | Notes |
|---|---|---|---|---|---|
| — | — | — | — | — | no endpoints declared yet |

Replace the placeholder row with real endpoints as the surface grows; delete
it once the table has a real row.

## Contracts

Serializer/response shapes, error envelopes, and pagination conventions go
here as the surface grows.

## Auth

How a caller authenticates and what carries authorization. Named here, ruled
by the project's own ADR once written.

## Versioning

How a breaking change to this surface is introduced and retired.
