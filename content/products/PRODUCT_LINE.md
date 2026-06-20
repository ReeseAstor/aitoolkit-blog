# AI ToolKit — Digital Product Production Line

**Mission:** Ship one high-quality, market-demanded digital product every week that is engineered to be useful, searchable, and shareable.

- **Catalog source:** `content/products/catalog.json`
- **Templates:** `content/products/templates/`
- **Upload-ready products:** `content/products/upload-ready/`
- **Generator script:** `scripts/generate_product.py`
- **Listing generator:** `scripts/generate_listing.py`

## Current production status

| ID | Product | Status | Format | Price | ETA |
|---|---|---|---|---|---|
| prod-001 | AI ToolKit SOP Vault Vol. 1 | **In progress** | SOP vault | $19 | Today |
| prod-002 | 50 Viral Short-Form Video Prompts | Planned | Prompt pack | $12 | Week 2 |
| prod-003 | The AI SEO Content System | Planned | Checklist + template | $17 | Week 3 |
| prod-004 | AI Ecommerce Description Templates | Planned | Template pack | $14 | Week 4 |
| prod-005 | Cold Email AI Swipe File | Planned | Swipe file | $16 | Week 5 |
| prod-006 | Social Media Content Machine | Planned | Checklist + prompts | $15 | Week 6 |
| prod-007 | AI Small Business Stack Playbook | Planned | Guide + workbook | $22 | Week 7 |
| prod-008 | AI Image Prompt Lab | Planned | Prompt pack | $13 | Week 8 |
| prod-009 | YouTube Creator AI Toolkit | Planned | Template pack | $18 | Week 9 |
| prod-010 | AI Content Creator Vault | Planned | Bundle | $37 | Week 10 |
| prod-011 | AI Marketing Operations Vault | Planned | Bundle | $39 | Week 11 |
| prod-012 | AI ToolKit Ultimate Bundle | Planned | Bundle | $97 | Week 12 |

## Demand engine: how products are selected

Every product must score high on four axes:

1. **Search demand** — uses a phrase real buyers type.
2. **Article relevance** — supports an existing high-traffic AI ToolKit article.
3. **Affiliate fit** — naturally references at least one program with real commission.
4. **Production speed** — can be built from templates in one focused session.

If a product idea fails any axis, it is deprioritized.

## Viral/product-market fit signals

- **Etsy:** 13 tags, descriptive file names, outcome-first title, seasonal refresh loops.
- **Gumroad:** Bundle-first pricing, "Vault" framing, direct social proof snippets.
- **Blog:** Each product gets a dedicated products page card + a bottom CTA in the matching article.
- **Newsletter:** Every launch is featured in the Monday edition with a short use-case story.
- **Social:** TikTok/Reels script + 3 static carousel slides are generated alongside the product.

## Quality bar

- Minimum 15 minutes of real manual editing before upload.
- No generic filler. Every page/section must be immediately usable.
- Affiliate links use `?via=aitoolkit` and `rel="nofollow sponsored"`.
- All files print/PDF-ready.

## Weekly workflow

1. **Monday:** Newsletter from last week's article.
2. **Tuesday:** Select next product from `catalog.json` based on traffic/season.
3. **Wednesday:** Generate the upload package with `scripts/generate_product.py`.
4. **Thursday:** Final edit + create Gumroad/Etsy listing from `scripts/generate_listing.py` output.
5. **Friday:** Add product card to blog products page; write social assets; send a targeted launch email.
6. **Sunday:** Memory/cron audit.

## File-naming convention

- `slug/` directory
- `README.md` — product overview, usage, affiliate CTAs
- `files/` — actual deliverable files
- `listing-gumroad.md` — Gumroad description
- `listing-etsy.md` — Etsy title, tags, description
- `social-launch-assets.md` — captions + carousel text
- `preview-images/` — Canva/Etsy mockups (placeholders; generate before upload)

## Next actions

- [x] Build catalog + production line docs
- [x] Build first upload-ready product
- [ ] Upload prod-001 to Gumroad and Etsy
- [ ] Add products showcase page to blog
- [ ] Schedule weekly Hermes cron job for product generation

