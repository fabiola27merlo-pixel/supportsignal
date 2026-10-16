# SupportSignal Demo Guide

This guide provides a short, repeatable demonstration of the event-driven SupportSignal workflow.

## Demo objective

Show that a real customer-initiated Intercom conversation automatically starts n8n, gathers account and system context, selects a route, and records the appropriate downstream action.

The recommended primary scenario is BrightDesk because it demonstrates that the system does not escalate every technical-sounding ticket to Engineering.

## Pre-demo checklist

Complete these checks before recording or presenting:

- [ ] Docker is running.
- [ ] n8n is reachable at `http://localhost:5678`.
- [ ] The FastAPI system-health service is reachable from n8n.
- [ ] The ngrok tunnel is running with the reserved development domain.
- [ ] Intercom points to `https://<your-ngrok-domain>/webhook/supportsignal/intercom`.
- [ ] The `conversation.user.created` subscription is enabled.
- [ ] The latest n8n workflow version is published.
- [ ] The workflow canvas contains no temporary test node or secret value.
- [ ] The browser does not display credentials, tokens, personal email, or unrelated company data.
- [ ] A fresh fictional Intercom contact and conversation are ready.

Start the tunnel if the computer has been restarted:

```bash
ngrok http 5678 --url https://<your-ngrok-domain>
```

## Suggested five-minute narrative

### 1. Explain the problem

SupportSignal helps a B2B SaaS support team decide whether a customer issue should stay with Support, escalate to Engineering, or require human review.

Emphasize that the system combines customer impact and live operational context rather than routing from ticket text alone.

### 2. Show the workflow architecture

In n8n, point out the two labeled entry paths:

- `PRODUCTION — Automatic Intercom Trigger`;
- `DEBUG — Manual Scenario Testing`.

Follow the production path from left to right:

```text
Intercom webhook
-> event filter
-> fetch one conversation
-> normalize
-> Salesforce + System Health
-> deterministic rules
-> Jev confidence routing when needed
-> downstream action
```

Do not open credential panels during the demo.

### 3. Create an inbound Intercom conversation

Create the BrightDesk conversation as the fictional customer, not as an administrator-generated outbound message.

Explain that Intercom emits `conversation.user.created` and that no one clicks `Execute workflow` in n8n.

### 4. Show the automatic n8n execution

Open the newest execution and show:

- the webhook received one event;
- `Only Conversation Events` accepted the conversation;
- `Get Intercom Conversation` fetched one record;
- the normalized customer and service fields;
- Salesforce account context;
- FastAPI system-health context;
- the final route and confidence.

For BrightDesk, the expected result is `SUPPORT_CONTINUE`.

### 5. Show the operational outcome

Return to Intercom and show the internal note added by SupportSignal. Explain that Engineering was not interrupted because the available evidence indicated a healthy service and low-risk support case.

Briefly mention the other two fictional scenarios:

- NovaTech demonstrates Engineering escalation, structured OpenAI handoff, Jira creation, and Slack notification.
- ApexLabs demonstrates the Human Review safety path.

## Scenario matrix

| Scenario | What it demonstrates | Expected visible result |
| --- | --- | --- |
| BrightDesk | Avoiding unnecessary escalation | Intercom support-continue note |
| NovaTech | High-impact technical escalation | Jira issue, Slack notification, Intercom note |
| ApexLabs | Safe handling of ambiguity | Intercom human-review note |

## Manual fallback

If Intercom is unavailable during a live presentation, use `Manual Trigger (Debug)` and select one of the existing fictional scenarios.

State clearly that this is a controlled fallback. The production architecture remains the automatic Intercom webhook demonstrated in the workflow.

## Troubleshooting

### Intercom sends the test request but no workflow starts

- Confirm the ngrok process is running.
- Confirm Intercom uses the reserved HTTPS domain and the production webhook path.
- Confirm the n8n workflow is published.
- Check that n8n is still reachable on port `5678`.

### A test request finishes after the event filter

This is expected for an Intercom verification `ping`. The filter discards it because it is not a conversation.

### Manual execution works but Intercom uses old behavior

The editor can run unpublished changes manually. External webhook events use the published workflow version. Publish the latest changes and try again.

### System-health lookup fails

Confirm FastAPI is running and that the URL configured in n8n is reachable from the n8n Docker container.

### The public URL stops working after a reboot

The reserved ngrok domain remains the same, but the local ngrok process must be restarted.

## Recording hygiene

- Use only fictional contacts and companies.
- Hide browser tabs containing email, credentials, billing, or unrelated work.
- Do not show n8n credential configuration.
- Do not show the ngrok authentication token.
- Prefer a fresh successful execution over historical failed test runs.
- Keep the workflow zoomed so the production path and decision branches are readable.

