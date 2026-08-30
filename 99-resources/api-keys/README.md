# API keys

The orchestrators and aggregators in this repo ([SpiderFoot](../../01-orchestrators/recursive-scanners/spiderfoot.md),
[BBOT](../../01-orchestrators/recursive-scanners/bbot.md),
[theHarvester](../../01-orchestrators/aggregators/theharvester.md),
[recon-ng](../../01-orchestrators/modular-frameworks/recon-ng.md)) are only as good
as the data sources you plug into them. Without keys, whole modules return nothing
- silently. This is which keys move the needle, roughly what they cost, and the
order to buy them in on a small budget.

Prices and free-tier limits change constantly. Treat every number here as
"approximately, last time anyone checked" and confirm on the provider's site.

## Where the keys go

| Tool | Config location |
|---|---|
| SpiderFoot | Settings page in the web UI, per-module |
| BBOT | `~/.bbot/secrets.yml` |
| theHarvester | `~/.theHarvester/api-keys.yaml` |
| recon-ng | `keys add <name> <value>` (stored in the workspace DB) |

## The keys that actually matter

| Service | What it adds | Free tier | Paid | Feeds |
|---|---|---|---|---|
| **Shodan** | Exposed devices, banners, historical ports | Very limited | ~$49 one-time membership for API + credits | SpiderFoot, BBOT, recon-ng |
| **VirusTotal** | Domain/IP/file reputation, passive DNS | Public API ~4 req/min, 500/day | Premium is enterprise-priced | reputation, SpiderFoot |
| **SecurityTrails** | Historical DNS/WHOIS, subdomains | ~50 queries/month | From ~$50/month | subfinder, Amass, recon-ng |
| **Hunter.io** | Corporate email addresses + patterns | ~25-50 searches/month | Tiered | theHarvester, recon-ng |
| **Have I Been Pwned** | Which breaches an email is in | none | ~$3.95/month | email-osint, SpiderFoot |
| **IPinfo** | ASN + org + geo in one call | 50k req/month token | Tiered | everything IP-related |
| **Censys** | Cert + host correlation | Limited free | Paid (no longer meaningfully free) | certificates, device-search |
| **GreyNoise** | Is this IP internet background noise | Community API | Enterprise | reputation |
| **AbuseIPDB** | Crowd-sourced abuse reports | ~1,000 checks/day | Tiered | reputation |
| **urlscan.io** | Higher scan/search limits | Free key raises limits | Paid | fingerprinting |
| **GitHub token** | Raises code-search rate limits | Free with any account | n/a | code-search, secret-scanning |

## Keys the newer categories need

Threat-intel, passive DNS and scan-search tools are key-gated in a different
way: most are free but require an account, and several changed policy recently.

| Service | What it adds | Free tier | Notes |
|---|---|---|---|
| **abuse.ch** (MalwareBazaar, URLhaus, ThreatFox) | Samples, malicious URLs, C2 indicators | Free `Auth-Key` from auth.abuse.ch | **Now mandatory on the query APIs** - a bare POST returns 401, so every pre-2025 snippet is dead. Signup is OAuth-only, so choose the persona that registers |
| **Netlas** | Scan data, certificates, WHOIS, subdomains from scans | 50 requests/day, 200 results per download | Free tier is personal use only |
| **Validin** | Passive DNS plus host-response pivots | Community tier, capped result count | Newer dataset; shallower history than the paid providers |
| **DNSDB** (Farsight / DomainTools) | The deepest resolution history | none | Paid. Buy only when the question genuinely reaches back years |
| **CIRCL Passive DNS** | CSIRT-collected resolution history | Free to vetted partners | Access is requested, not self-served - ask before you need it |
| **mnemonic PassiveDNS** | Resolution history, both directions | Keyless for TLP:white data | The one passive DNS source that needs no account at all |
| **Intelligence X** | Leaks, pastes, darknet crawls by selector | Free account, limited daily lookups | The API key is separate from the web account |
| **Recorded Future Triage** | Sandbox reports, family and config extraction | Free research account | Free-tier submissions are public |
| **ONYPHE** | Scan and threat data, own query language | Free view, standard filters only | Advanced filters are plan-gated; a docs query can return zero because of your licence |
| **urlquery** | URL scans, IDS and traffic detection | Anonymous search; free key for the CLI | Searching costs nothing and tells the operator nothing |

Assume every submission on a free tier is public unless the provider says
otherwise, and read [../../13-threat-intel/README.md](../../13-threat-intel/README.md)
before you upload anything.

## Buy in this order on a small budget

1. **Free keys first, all of them.** IPinfo, VirusTotal (public), AbuseIPDB,
   GreyNoise community, Hunter.io free tier, SecurityTrails free tier, urlscan.io,
   an abuse.ch Auth-Key, Netlas, and a GitHub personal access token. Zero cost,
   and they light up most modules.
2. **Shodan membership (~$49, one-time).** The single best paid pickup. It is a
   one-off, not a subscription, and it unlocks device/exposure data that nothing
   free replicates. Watch for the periodic sales.
3. **Have I Been Pwned (~$3.95/month)** if you do any email or account work. Cheap,
   high signal, hard to substitute.
4. **SecurityTrails or Censys paid** only once you are doing enough
   subdomain/cert/history work that the free tiers throttle you. This is the point
   where cost climbs; do not start here.

## Notes

- Keys are secrets. Do not commit them. `~/.bbot/secrets.yml` and the recon-ng
  workspace DB live outside the repo for a reason - keep it that way.
- A key that works today can be revoked or re-priced tomorrow. If a module goes
  quiet, check the key before you conclude the target has nothing.
- Some "free" tiers require you to agree to terms that limit commercial use or
  data retention. Read them if the work is billable.
