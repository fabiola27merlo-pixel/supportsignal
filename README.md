# SupportSignal

AI-assisted Support-to-Engineering escalation system for B2B SaaS.

SupportSignal analyzes support tickets, enriches them with customer and system context, and determines whether a case should:

- stay with Support
- escalate to Engineering
- go to Human Review

The system combines deterministic business rules, probabilistic AI decisioning, and structured technical handoffs.

## Problem

Growing SaaS companies often struggle with inconsistent escalation decisions between Support and Engineering.

Support teams may:

- escalate issues that could be handled without Engineering
- miss incidents that require urgent technical investigation
- lack enough customer and system context to make a confident decision
- provide incomplete handoff information to Engineering

SupportSignal is designed to make that process faster, more consistent, and auditable.

## Architecture

- Intercom — Support conversations
- Salesforce — Customer and account context
- FastAPI — System health context
- n8n — Workflow orchestration
- Jev — Probabilistic decisioning
- OpenAI — Technical handoff generation
- Jira — Engineering escalation
- Slack — Internal notifications
- Supabase — Decision audit log

## Project Status

🚧 In development