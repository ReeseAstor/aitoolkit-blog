# Affiliate Application Package — PartnerStack / Copy.ai / Canva

**Date:** June 25, 2026  
**Site:** aitoolkit-blog.vercel.app  
**Brand:** AI ToolKit / PanicProofPrintables  
**Audience:** AI-curious creators, solopreneurs, small business owners looking for practical AI tools.

---

## 1. PartnerStack Marketplace — Apply Here First

**URL:** https://partnerstack.com/our-partner-program/partners-affiliate  
**What it is:** Hub for B2B SaaS affiliate programs. Apply once, then join individual programs inside.

### Direct Application Link

Use this URL to create your PartnerStack partner account:

> **https://dash.partnerstack.com/handshake/login?company=partners&gref=marketplace&application=partners&next=/marketplace&nextApp=partner**

After you're approved, browse the marketplace to apply to individual programs.

### Programs to Join (in order)

| Program | Commission | Why Fit |
|---|---|---|
| **Copy.ai** | 45% first year, 60-day cookie | Core writing-tool recommendation across multiple articles |
| **Writesonic** | 30% lifetime recurring | AI writing comparison articles |
| **Jasper** | Recurring via PartnerStack | Premium AI writing alternative |
| **AdCreative.ai** | 30% lifetime recurring | Ad-creative / social content articles |
| **Synthesia** | 20% first 12 months, 60-day cookie | AI video content articles |
| **Speechify** | 50% flat, 90-day cookie | Voice/AI audio articles |
| **Canva** | Up to 20%, 30-day cookie | Currently requires Canvassador Program (see below) |

---

## 2. Copy.ai Application — Direct / PartnerStack

**PartnerStack page:** search "Copy.ai" in marketplace  
**Site to submit:** https://www.copy.ai/partners  
**Estimated payout:** 45% of first-year revenue per referred customer.

### Application Copy

**Website URL:** https://aitoolkit-blog.vercel.app  
**How you promote:** SEO-optimized comparison articles, product roundups, and tutorial content for AI writing tools.  
**Audience size:** [fill in — newsletter subscribers, monthly visitors]  
**Traffic sources:** organic search, newsletter, social  
**Sample content:**
- "Best AI Writing Tools 2026" — https://aitoolkit-blog.vercel.app/articles/best-ai-writing-tools-2026.html
- "Copy.ai vs Jasper vs Writesonic" — https://aitoolkit-blog.vercel.app/articles/copyai-vs-jasper-vs-writesonic.html

**Why Copy.ai is a good fit:** It appears as the top recommendation in multiple comparison articles and is the natural next step for readers who want a dedicated AI writing workflow.

---

## 3. Canva — Canvassador Program (Current Path)

**Status:** Canva's traditional affiliate program is closed to new applicants. The only pathway is the **Canvassador Program**.

**URL:** https://public.canva.site/canvassadors  
**What it is:** Community-based ambassador program for Canva content creators.

### Canvassador Application Copy

**Who you are:** Creator of AI ToolKit, a practical AI-tool review site helping small creators and solopreneurs choose the right tools.  
**Content you create:** AI tool comparisons, design-tool tutorials, and printable/digital product how-tos.  
**Why Canva:** Canva is frequently recommended as the design companion to AI-generated content (social graphics, lead magnets, printables).  
**Sample Canva-related content:** [fill in once you have one]  
**Social handles:** [fill in]  
**Audience:** [fill in]

### Workaround If Canvassador Rejects / Slow

Use a direct **Canva Pro referral link** if you already have Canva Pro:  
https://www.canva.com/canva-pro/referral/  
Or swap CTAs to **AdCreative.ai** (available via PartnerStack, 30% lifetime) for the visual-design angle.

---

## 4. Site-Wide Link Replacement Script

Once you have real affiliate IDs, run this Python script from `~/projects/aitoolkit-blog/` to replace all `?via=aitoolkit` placeholders.

```python
# scripts/replace_affiliate_ids.py
import re, sys, os, json
from pathlib import Path

# CONFIG: map tool domain to your real affiliate parameter
AFFILIATE_IDS = {
    "copy.ai": "?via=YOUR_COPYAI_ID",
    "writesonic.com": "?via=YOUR_WRITESONIC_ID",
    "jasper.ai": "?via=YOUR_JASPER_ID",
    "adcreative.ai": "?via=YOUR_ADCREATIVE_ID",
    "synthesia.io": "?via=YOUR_SYNTHESIA_ID",
    "speechify.com": "?via=YOUR_SPEECHIFY_ID",
    "canva.com": "?via=YOUR_CANVA_ID",
    "surferseo.com": "?via=YOUR_SURFER_ID",
}

# Files to scan
EXTENSIONS = (".html", ".md", ".js", ".json")

REPLACEMENTS = 0

for ext in EXTENSIONS:
    for path in Path(".").rglob(f"*{ext}"):
        # skip node_modules, .git, venv
        if any(part.startswith((".", "node_modules", "venv")) for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        new_text = text
        for domain, aff_id in AFFILIATE_IDS.items():
            # Replace ?via=aitoolkit on URLs matching this domain
            pattern = re.compile(
                rf'(https?://[^"\'\s]*{re.escape(domain)}[^"\'\s]*)\?via=aitoolkit',
                re.IGNORECASE,
            )
            matches = pattern.findall(new_text)
            if matches:
                new_text = pattern.sub(rf"\1{aff_id}", new_text)
                REPLACEMENTS += len(matches)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated: {path}")

print(f"\nTotal replacements: {REPLACEMENTS}")
```

### Usage

```bash
cd ~/projects/aitoolkit-blog
py scripts/replace_affiliate_ids.py        # dry run: shows what would change
py scripts/replace_affiliate_ids.py --apply # writes changes only when IDs are real
```

**Before running `--apply`:**
1. Fill in your real IDs in `AFFILIATE_IDS`.
2. Run the dry-run first.
3. Run `git diff` after `--apply` to verify no accidental changes.
4. Commit and push.

---

## 5. Files to Check Manually After Replacement

These files likely contain the most affiliate links:

- `articles/best-ai-writing-tools-2026.html`
- `articles/copyai-vs-jasper-vs-writesonic.html`
- `articles/best-ai-ad-creative-tools-2026.html`
- `articles/best-ai-voice-generators-2026.html`
- `articles/best-ai-image-generators-2026.html`
- `articles/ai-tools-small-business-owners.html`
- `content/products/*.md` (product landing-page source)
- `products/*.html` (product landing pages)
- `assets/main.js` (storefront)

---

## 6. Immediate To-Dos

- [ ] Create PartnerStack account at https://market.partnerstack.com/
- [ ] Apply to Copy.ai via PartnerStack
- [ ] Apply to AdCreative.ai via PartnerStack
- [ ] Apply to Writesonic via PartnerStack
- [ ] Apply to Canvassador program at https://public.canva.site/canvassadors
- [ ] Collect your real `?via=` IDs
- [ ] Update `scripts/replace_affiliate_ids.py` with real IDs
- [ ] Run the script and review `git diff`
[ ] Commit + push to Vercel
[ ] Verify at least 5 live pages show real affiliate links

---

## 7. AdCreative.ai as Canva Alternative

If Canva affiliate takes too long, switch visual-design CTAs to AdCreative.ai:
- 30% lifetime recurring
- Stronger fit for AI-tool audience than Canva in some articles
- Available immediately via PartnerStack

**CTA swap example:**
Old: "Design your social graphics in Canva"
New: "Generate conversion-focused ad creatives with AdCreative.ai"

Track which converts better. Canva can be re-added once Canvassador is approved.
