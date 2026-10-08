# AI ToolKit Pipeline Run Log

## 2026-10-07 — Article 105: Google Business Profile workflow stack
- **Article:** `best-ai-tools-google-business-profile-2026.html` — "Best AI Tools for Google Business Profile in 2026: Copy.ai vs Canva vs Jasper vs Surfer" (category: Workflow Stack, 2,463 words, 11 min read)
- **Topic rationale:** Google Business Profile / local SEO had zero dedicated coverage (only passing mentions in 6 niche-stack articles); workflow pulls in 5 of 8 affiliate programs (Copy.ai, Canva, Jasper, Surfer, Speechify); pre-holiday October timing.
- **Pricing verification (web_search/web_extract hard-timeout 420s this run — fell back to curl of official pricing pages + Python text probes):**
  - Copy.ai: Chat $29/mo monthly / $24/mo annual ($288/yr), 5 seats, unlimited words — verified live from copy.ai/prices
  - Canva: Pro $144/yr / Business $250/yr per person, Teams discontinued for new signups — from Oct 5 2026 official-page sweep (canva.com/pricing bot-walled this run, 14KB shell)
  - Jasper: Pro $59/seat/mo yearly, $69 monthly, 7-day trial, Creator eliminated — verified live from jasper.ai/pricing
  - Surfer: Discovery $49/mo billed yearly, Standard $99, Pro $182, AI Visibility track $82/mo — verified live from surferseo.com/pricing; consistent with all recent article mentions
  - Speechify: Premium $29/mo monthly verified live from speechify.com/pricing; $139/yr from Oct 5 sweep
- **Cross-article drift check:** Surfer/Jasper/Canva/Speechify/Copy.ai mentions in recent 12 articles all consistent — no stale pricing found this run.
- **Verification:** 17-check ad-hoc verifier PASS (meta desc 153 chars, 3 CTA boxes, 18 affiliate anchors, all 5 domains with ≥1 tracked link, coverage per-domain TRUE ×5). Node validator: ARTICLES 103 entries (new slug at top) VALID, PRODUCTS 24 entries VALID.
- **Publish:** commit `a3aa6c3` on master, 2 files changed (article + main.js), push verified via `git ls-tree -r origin/master` (blob 4da4d65) and empty `git diff`. Live 200 at https://aitoolkit-blog.vercel.app/articles/best-ai-tools-google-business-profile-2026 (served extensionless after 308), title + 14 tracked links confirmed in live HTML.
- **Ops notes this run:** sandbox `python` via POSIX path doubles path (use `C:/...` forward-slash native paths); cron-mode blocks `rm -rf` on absolute dirs — clean temp files individually; write_file landed at correct path first try, no /c/c/ stray.