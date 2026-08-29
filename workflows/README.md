# Workflows

End-to-end playbooks. The category directories tell you what each tool does;
these tell you what to run, in what order, and **why that order**.

Each playbook starts from a single artifact and chains specific tool files with
the reasoning between the steps - including where to stop without authorisation.

| Playbook | Start from | Ends with |
|---|---|---|
| [Domain investigation](domain-investigation.md) | A domain name | Infrastructure, history, ownership pivots, and lookalikes |
| [Phishing email triage](phishing-email-triage.md) | A suspicious `.eml` | Real origin, campaign scope, and what to tell the business |
| [Username to identity](username-to-identity.md) | A handle or alias | Corroborated accounts, and an honest confidence assessment |
| [Onion service investigation](onion-service-investigation.md) | A `.onion` address | What the service is, and what links it to the clearweb |
| [Dark web exposure monitoring](dark-web-exposure-monitoring.md) | An organisation name | Whether its data is being published, and evidence to escalate |
| [Dorking to documents](dorking-to-documents.md) | A domain or company | Exposed files, their metadata, and the leads inside it |

## The order is the point

Three rules run through all of them:

1. **Passive before active.** Certificate transparency, archives, and registries
   cost nothing and leave no trace. Exhaust them before you touch the target -
   you cannot un-touch it.
2. **Stop at the authorisation boundary.** Every playbook marks where the next
   step becomes intrusive. Written authorisation before you cross it. See
   [../LEGAL.md](../LEGAL.md).
3. **Corroborate before concluding.** Shared hosting, shared certificate SANs, a
   shared username, and a reverse-image "match" are all leads, not conclusions.
   The playbooks flag each trap where it arises.

The dark web playbooks add a fourth: **observation is not interaction.** Loading
a hidden service is a request its operator can see; registering, messaging, or
buying is a different activity with a different legal footing. Read the dark web
section of [../LEGAL.md](../LEGAL.md) before either of them.

## Writing another one

A playbook earns its place if it answers a question an investigator actually
arrives with. Keep the structure: numbered steps, the tool files linked inline,
a sentence on *why* each step sits where it does, and an explicit note where the
work becomes intrusive or legally sensitive.
