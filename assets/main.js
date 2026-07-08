// AI ToolKit - Main JavaScript
// Dynamic article loading + newsletter handling

const ARTICLES = [
        {
        slug: "best-ai-tools-website-copy-2026",
        title: "Best AI Tools for Writing High-Converting Website Copy in 2026: Copy.ai vs Jasper vs Writesonic",
        excerpt: "Write high-converting website copy in minutes. Compare Copy.ai, Jasper, and Writesonic for homepages, about pages, and service pages with verified 2026 pricing.",
        category: "Comparison",
        date: "2026-07-08",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-tools-employee-training-onboarding-2026",
        title: "Best AI Tools for Employee Training and Onboarding in 2026: Build a Complete L&D Stack",
        excerpt: "Build a complete AI-powered employee training and onboarding stack in 2026. We tested Synthesia, Copy.ai, Canva, and Speechify for L&D teams.",
        category: "Guides",
        date: "2026-07-07",
        readTime: "7 min read"
    },
    {
        slug: "best-ai-tools-personal-branding-2026",
        title: "Best AI Tools for Building a Personal Brand in 2026: Copy.ai vs Canva vs Synthesia vs AdCreative.ai",
        excerpt: "Build a personal brand in 2026 with AI tools. Compare Copy.ai, Canva, Synthesia, and AdCreative.ai for bios, graphics, video, and ads with verified pricing.",
        category: "Comparison",
        date: "2026-07-06",
        readTime: "12 min read"
    },
    {
        slug: "how-to-repurpose-content-with-ai-2026",
        title: "How to Repurpose One Piece of Content Into 10+ Formats Using AI (2026)",
        excerpt: "Turn one blog post into videos, podcasts, social graphics, ads, and emails using AI tools. Step-by-step repurposing workflow with Copy.ai, Synthesia, Canva, and more.",
        category: "Content Strategy",
        date: "2026-07-05",
        readTime: "12 min"
    },
    {
        slug: "best-ai-tools-local-businesses-2026",
        title: "Best AI Tools for Local Businesses in 2026: Copy.ai vs Canva vs AdCreative.ai vs Surfer",
        excerpt: "Local businesses use AI to write listings, design flyers, run ads, and rank locally in 2026. We compare Copy.ai, Canva, AdCreative.ai, and Surfer with verified pricing and real workflows.",
        category: "Comparison",
        date: "2026-07-05",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-pitch-decks-presentations-2026",
        title: "Best AI Tools for Pitch Decks and Presentations in 2026: Canva vs Copy.ai vs Synthesia vs Jasper vs Speechify",
        excerpt: "Build pitch decks and presentations 10x faster with AI in 2026. Compare Canva, Copy.ai, Synthesia, Jasper, and Speechify for slides, video, and narration with verified pricing and workflows.",
        category: "Comparison",
        date: "2026-07-03",
        readTime: "12 min read"
    },
    {
        slug: "best-ai-tools-real-estate-marketing-2026",
        title: "Best AI Tools for Real Estate Marketing in 2026: Copy.ai vs Canva vs Synthesia vs AdCreative.ai vs Surfer",
        excerpt: "We tested the top AI tools for real estate marketing in 2026. Compare Copy.ai, Canva, Synthesia, AdCreative.ai, and Surfer for listings, ads, video, and local SEO with verified pricing.",
        category: "Comparison",
        date: "2026-07-02",
        readTime: "12 min read"
    },
    {
        slug: "ai-freelancer-stack-playbook-2026",
        title: "The AI Freelancer Stack Playbook: 40+ Prompts for a One-Person Business in 2026",
        excerpt: "Run a one-person business on AI without a $300/month tool pile. The 5-function Freelancer Stack, 30-day rollout, and 40+ copy-paste prompts built around Copy.ai, Canva, Synthesia, Speechify, and Bonsai.",
        category: "Guide + Product",
        date: "2026-07-01",
        readTime: "11 min read"
    },
        {
        slug: "best-ai-tools-freelancers-solopreneurs-2026",
        title: "Best AI Tools for Freelancers and Solopreneurs in 2026: Copy.ai vs Canva vs Synthesia vs Speechify vs AdCreative.ai",
        excerpt: "The 2026 AI stack freelancers and solopreneurs use to land clients, deliver work, and grow a one-person business. Compare Copy.ai, Canva, Synthesia, Speechify, and AdCreative.ai with verified pricing.",
        category: "Guide",
        date: "2026-07-01",
        readTime: "12 min read"
    },
    {
        slug: "best-ai-tools-coaches-consultants-2026",
        title: "Best AI Tools for Coaches and Consultants in 2026: Copy.ai vs Canva vs Synthesia vs Speechify vs AdCreative.ai",
        excerpt: "The 2026 AI stack coaches and consultants actually use to land clients, deliver sessions, and grow a practice. Compare Copy.ai, Canva, Synthesia, Speechify, and AdCreative.ai with verified pricing.",
        category: "Guide",
        date: "2026-06-30",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-short-form-video-2026",
        title: "Best AI Tools for Short-Form Video Content in 2026: Synthesia vs Canva vs Copy.ai vs AdCreative.ai",
        excerpt: "We tested the top AI tools for short-form video and Reels in 2026. Compare Synthesia, Canva, Copy.ai, and AdCreative.ai for scripts, avatars, graphics, and high-converting Shorts with real pricing and workflows.",
        category: "Comparison",
        date: "2026-06-29",
        readTime: "12 min read"
    },
    {
        slug: "best-ai-tools-linkedin-content-2026",
        title: "Best AI Tools for LinkedIn Content and Thought Leadership in 2026: Copy.ai vs Jasper vs Canva vs Synthesia",
        excerpt: "We tested the top AI tools for LinkedIn thought leadership in 2026. Compare Copy.ai, Jasper, Canva, and Synthesia for posts, carousels, video, and brand voice. Real pricing and workflows.",
        category: "Comparison",
        date: "2026-06-28",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-landing-page-tools-2026",
        title: "Best AI Tools for High-Converting Landing Pages in 2026: Copy.ai vs Jasper vs Canva vs AdCreative.ai vs Surfer",
        excerpt: "We tested the top AI tools for building high-converting landing pages in 2026. Compare Copy.ai, Jasper, Canva, AdCreative.ai, and Surfer for copy, design, ads, and SEO optimization.",
        category: "Comparison",
        date: "2026-06-27",
        readTime: "12 min read"
    },
    {
        slug: "best-ai-tools-lead-magnets-opt-in-funnels-2026",
        title: "Best AI Tools for Lead Magnets & Opt-In Funnels in 2026",
        excerpt: "Build high-converting lead magnets and opt-in funnels with AI in 2026. Compare Copy.ai, Canva, AdCreative.ai, and Synthesia for copy, design, ads, and video.",
        category: "Guide",
        date: "2026-06-26",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-webinar-tools-2026",
        title: "Best AI Tools for Webinars and Video Presentations in 2026: Copy.ai vs Canva vs Synthesia vs Speechify",
        excerpt: "The 2026 AI stack for building, hosting, and repurposing webinars and video presentations without a camera crew. Compare Copy.ai, Canva, Synthesia, and Speechify with verified pricing.",
        category: "Guide",
        date: "2026-06-25",
        readTime: "11 min read"
    },
    {
        slug: "ai-ecommerce-marketing-command-center-2026",
        title: "AI Ecommerce Marketing Command Center: 35 Prompts + 12 Checklists for 2026",
        excerpt: "Turn your Shopify, Etsy, or WooCommerce store into a 90-minute weekly content machine with 35 AI prompts and 12 production checklists built around Copy.ai, Canva, AdCreative.ai, and Synthesia.",
        category: "Guide + Product",
        date: "2026-06-25",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-tools-ecommerce-marketing-2026",
        title: "Best AI Tools for Ecommerce Marketing in 2026: Copy.ai vs Canva vs AdCreative.ai vs Synthesia",
        excerpt: "We tested the top AI tools for ecommerce marketing in 2026. Compare Copy.ai, Canva, AdCreative.ai, and Synthesia for product copy, ads, store visuals, and product demo videos.",
        category: "Comparison",
        date: "2026-06-24",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-email-marketing-2026",
        title: "Best AI Tools for Email Marketing & Newsletters in 2026: Copy.ai vs Jasper vs Writesonic vs Surfer",
        excerpt: "We tested the top AI tools for email marketing and newsletter growth in 2026. Compare Copy.ai, Jasper, Writesonic, Surfer, Canva, and AdCreative.ai for subject lines, sequences, landing pages, and list growth.",
        category: "Comparison",
        date: "2026-06-23",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-for-blog-content-2026",
        title: "Best AI Tools for Blog Content Creation in 2026: Copy.ai vs Writesonic vs Jasper vs Surfer",
        excerpt: "We tested the top AI tools for blog writing and SEO in 2026. Compare Copy.ai, Writesonic, Jasper, and Surfer for output quality, SEO features, pricing, and which one delivers the best ROI for content creators and small businesses.",
        category: "Comparison",
        date: "2026-06-21",
        readTime: "12 min read"
    },
    {
        slug: "best-ai-tools-podcast-production-2026",
        title: "Best AI Tools for Podcast Production in 2026: The Show Notes, Audiograms & Repurposing Stack",
        excerpt: "The exact 4-tool AI stack to ship a podcast episode in 2026 — Copy.ai for show notes, Canva for cover art and audiograms, Synthesia for video clips, and Surfer for episode SEO. With verified pricing.",
        category: "Guide",
        date: "2026-06-19",
        readTime: "10 min read"
    },
    {
        slug: "how-to-repurpose-content-with-ai-2026",
        title: "How to Repurpose One Piece of Content Into 10 With AI (2026 Workflow)",
        excerpt: "Turn one blog post or video into 10+ assets with AI. The exact 4-tool repurposing stack — Copy.ai for text, Canva for graphics, Synthesia for video, Speechify for audio — with real 2026 pricing.",
        category: "Guide",
        date: "2026-06-18",
        readTime: "10 min read"
    },
    {
        slug: "how-to-create-online-course-with-ai-2026",
        title: "How to Create an Online Course With AI in a Weekend (2026 Step-by-Step)",
        excerpt: "The exact 4-tool AI workflow to take a course from blank page to buy-now button in a weekend — scripts with Copy.ai, camera-free video with Synthesia, slides in Canva, and audio with Speechify.",
        category: "Guide",
        date: "2026-06-17",
        readTime: "9 min read"
    },
        {
        slug: "best-ai-tools-online-course-creators-2026",
        title: "Best AI Tools for Online Course Creators in 2026: Synthesia vs Canva vs Copy.ai vs Speechify",
        excerpt: "The exact AI stack we use to build and sell online courses in 2026. Compare Synthesia, Canva, Copy.ai, and Speechify for video lessons, slides, sales pages, and audio versions.",
        category: "Guide",
        date: "2026-06-17",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-cold-email-outreach-2026",
        title: "Best AI Tools for Cold Email Outreach in 2026: Copy.ai vs Writesonic vs Jasper",
        excerpt: "We tested the top AI tools for cold email outreach in 2026. Compare Copy.ai, Writesonic, Jasper, and AdCreative.ai for reply rates, personalization, and SDR workflows.",
        category: "Comparison",
        date: "2026-06-15",
        readTime: "11 min read"
    },
    {
        slug: "best-ai-tools-social-media-content-2026",
        title: "Best AI Tools for Social Media Content Creation in 2026: Copy.ai vs Canva vs AdCreative.ai vs Synthesia",
        excerpt: "The exact AI stack we use to ship a week of social content in one afternoon. Tested Copy.ai, Canva, AdCreative.ai, and Synthesia for captions, graphics, ads, and video.",
        category: "Comparison",
        date: "2026-06-14",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-tools-ecommerce-product-descriptions-2026",
        title: "Best AI Tools for Ecommerce Product Descriptions in 2026: Copy.ai vs Writesonic vs Jasper",
        excerpt: "We tested the top AI tools for ecommerce product descriptions in 2026. Compare Copy.ai, Writesonic, Jasper, and AdCreative.ai for bulk product copy, SEO, and conversion.",
        category: "Comparison",
        date: "2026-06-13",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-ad-creative-tools-2026",
        title: "Best AI Ad Creative Generators in 2026: AdCreative.ai vs Canva vs Predis.ai",
        excerpt: "We tested the top AI ad creative tools of 2026. Compare AdCreative.ai, Canva, Predis.ai, and Creatify for ad quality, pricing, and conversion prediction.",
        category: "Comparison",
        date: "2026-06-09",
        readTime: "9 min read"
    },
    {
        slug: "best-ai-voice-generators-2026",
        title: "Best AI Voice Generators in 2026: Speechify vs ElevenLabs vs PlayHT",
        excerpt: "We tested Speechify, ElevenLabs, and PlayHT side by side. Honest comparison of voice quality, languages, pricing, and the real winner for creators.",
        category: "Comparison",
        date: "2026-06-08",
        readTime: "9 min read"
    },
    {
        slug: "best-ai-tools-youtube-creators-2026",
        title: "Best AI Tools for YouTube Creators in 2026: The Complete Stack",
        excerpt: "The exact AI stack YouTube creators use in 2026 to script, voice, edit, thumbnail, and publish faster. Tested tools with real pricing.",
        category: "Guide",
        date: "2026-06-08",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-image-generators-2026",
        title: "Best AI Image Generators in 2026: From Midjourney to DALL-E",
        excerpt: "We tested the top AI image generators of 2026. Compare Midjourney, DALL-E, Stable Diffusion, and ImagineArt for quality, price, and ease of use.",
        category: "Comparison",
        date: "2026-06-08",
        readTime: "10 min read"
    },
    {
        slug: "best-ai-writing-tools-2026",
        title: "Best AI Writing Tools in 2026: The Only 5 You Actually Need",
        excerpt: "We tested 20+ AI writing tools. These 5 stand out for content creators — from blog posts to marketing copy.",
        category: "Reviews",
        date: "2026-06-08",
        readTime: "8 min read"
    },
    {
        slug: "copyai-vs-jasper-vs-writesonic",
        title: "Copy.ai vs Jasper vs Writesonic: Which AI Writer Wins in 2026?",
        excerpt: "Side-by-side comparison of the top 3 AI writing platforms. Pricing, features, and real output quality tested.",
        category: "Comparison",
        date: "2026-06-07",
        readTime: "12 min read"
    },
    {
        slug: "ai-tools-small-business-owners",
        title: "10 AI Tools Every Small Business Owner Should Use in 2026",
        excerpt: "From automating emails to generating social content — these AI tools save 10+ hours per week.",
        category: "Guide",
        date: "2026-06-06",
        readTime: "10 min read"
    }
];

const PRODUCTS = [
    {
        slug: "ai-freelancer-stack-playbook",
        title: "The AI Freelancer Stack: 2026 Playbook",
        excerpt: "5-function system, 30-day rollout, and 40+ copy-paste prompts for running a one-person business on AI. Built around Copy.ai, Canva, Synthesia, Speechify, and Bonsai.",
        price: "$22",
        category: "Guide + Workbook + Prompt Pack",
        image: "/assets/previews/ai-freelancer-stack-playbook/ai-freelancer-stack-playbook-preview-hero.png"
    },
    {
        slug: "ai-ecommerce-marketing-command-center",
        title: "AI Ecommerce Marketing Command Center (2026 Edition)",
        excerpt: "35 copy-paste AI prompts + 12 production checklists for Shopify, Etsy, and WooCommerce sellers. Built around Copy.ai, Canva, AdCreative.ai, and Synthesia.",
        price: "$17",
        category: "Prompt Pack + Checklist",
        image: "/assets/previews/ai-ecommerce-marketing-command-center/ai-ecommerce-marketing-command-center-preview-hero.png"
    },
    {
        slug: "adhd-refill-panic-binder",
        title: "The ADHD Refill Panic Binder (2026 Edition)",
        excerpt: "60+ printable + fillable pages for medication refills, pharmacy calls, appointments, prior auth, and provider notes. Built for U.S. adults with ADHD. Includes Google Sheets bonus.",
        price: "$29",
        category: "Printable Binder"
    },
    {
        slug: "ai-online-course-creator-kit",
        title: "The AI Online Course Creator Kit (2026 Edition)",
        excerpt: "Build, record, and launch a sellable online course in a weekend. 6 modules, 60+ prompts, 9 templates, sales page + email sequence, and a launch checklist — using Copy.ai, Synthesia, Canva, and Speechify.",
        price: "$24",
        category: "Kit + Templates"
    },
    {
        slug: "ai-toolkit-sop-vault-v1",
        title: "AI ToolKit SOP Vault Vol. 1",
        excerpt: "15 drop-in marketing SOPs with exact prompts. LinkedIn, newsletters, SEO briefs, cold outreach, YouTube scripts, and more.",
        price: "$19",
        category: "SOP Vault"
    },
    {
        slug: "50-viral-video-prompts",
        title: "50 Viral Short-Form Video Prompts",
        excerpt: "Hook-first prompts for Reels, TikTok, and YouTube Shorts using AI voice + AI video tools.",
        price: "$12",
        category: "Prompt Pack"
    },
    {
        slug: "ai-seo-content-system",
        title: "The AI SEO Content System: 2026 Edition",
        excerpt: "25-point SEO checklist + content-brief template + audit matrix + 5 AI prompt sequences for ranking AI-assisted content.",
        price: "$17",
        category: "Checklist + Template"
    },
    {
        slug: "ai-ecommerce-description-templates",
        title: "50+ Shopify & Amazon Product Description Templates | AI Prompts for Ecommerce Sellers",
        excerpt: "Write 100+ high-converting product descriptions in one afternoon. Includes 50+ templates for Amazon, Shopify, Etsy + Copy.ai prompts that match your brand voice.",
        price: "$14",
        category: "Template Pack"
    },
    {
        slug: "cold-email-ai-swipes",
        title: "Cold Email AI Swipe File",
        excerpt: "40 cold email sequences that book meetings. Includes personalized first-line prompts and 3-email follow-ups.",
        price: "$16",
        category: "Swipe File"
    },
    {
        slug: "ai-social-media-content-calendar",
        title: "Social Media Content Machine: 30-Day AI Content Calendar",
        excerpt: "30-day social media calendar + 50 post templates + engagement hooks + hashtag research. Built for Copy.ai, Canva, and AdCreative.ai.",
        price: "$15",
        category: "Checklist + Prompts"
    },
    {
        slug: "ai-small-business-stack-playbook",
        title: "The AI Small Business Stack: 2026 Playbook",
        excerpt: "The 9-function AI stack framework, tool picks, 30-day rollout, ROI calculator, and 15 prompts to save 10+ hours a week.",
        price: "$22",
        category: "Guide + Workbook"
    },
    {
        slug: "ai-image-prompt-lab",
        title: "Midjourney + DALL-E Prompt Lab",
        excerpt: "100 market-ready image prompts for product mockups, ads, thumbnails, and social — plus the formula and parameter cheat sheet.",
        price: "$13",
        category: "Prompt Pack"
    },
    {
        slug: "youtube-creator-ai-toolkit",
        title: "YouTube Creator AI Toolkit",
        excerpt: "5 script frameworks, 30 hooks, thumbnail prompts, 25 title patterns, and an SEO description template. Cut prep to under 2 hours.",
        price: "$18",
        category: "Template Pack"
    },
    {
        slug: "ai-content-creator-vault",
        title: "AI Content Creator Vault (Bundle)",
        excerpt: "Video prompts + social calendar + YouTube toolkit. $45 of content tools for $37 — free updates for life.",
        price: "$37",
        category: "Bundle",
        image: "/assets/previews/ai-content-creator-vault/ai-content-creator-vault-preview-hero.png"
    },
    {
        slug: "ai-marketing-operations-vault",
        title: "AI Marketing Operations Vault (Bundle)",
        excerpt: "SOPs + SEO system + cold email swipes. The complete AI marketing operation — $52 of tools for $39.",
        price: "$39",
        category: "Bundle",
        image: "/assets/previews/ai-marketing-operations-vault/ai-marketing-operations-vault-preview-hero.png"
    },
    {
        slug: "aitoolkit-ultimate-bundle",
        title: "AI ToolKit Ultimate Bundle",
        excerpt: "All 9 products in one library — SOPs, prompts, templates, swipes, and systems. $146 of tools for $97, free updates for life.",
        price: "$97",
        category: "Bundle",
        image: "/assets/previews/aitoolkit-ultimate-bundle/aitoolkit-ultimate-bundle-preview-hero.png"
    }
];

const ARTICLE_ARCHIVE = [
    {
        slug: "ai-video-tools-creators",
        title: "AI Video Creation Tools Compared: Synthesia vs Colossyan vs HeyGen",
        excerpt: "Create professional videos without a camera. We compare the top AI video platforms for creators and marketers.",
        category: "Comparison",
        date: "2026-06-05",
        readTime: "9 min read"
    },
    {
        slug: "ai-seo-tools-rank-higher",
        title: "AI SEO Tools That Actually Help You Rank Higher in 2026",
        excerpt: "Surfer, Frase, and MarketMuse go head-to-head. Which AI SEO tool delivers the best ROI?",
        category: "Guide",
        date: "2026-06-04",
        readTime: "7 min read"
    }
];

const TOOLS = [
    {
        name: "Copy.ai",
        icon: "✍️",
        commission: "45% for 1st year",
        slug: "copyai-vs-jasper-vs-writesonic"
    },
    {
        name: "Writesonic",
        icon: "📝",
        commission: "30% lifetime",
        slug: "copyai-vs-jasper-vs-writesonic"
    },
    {
        name: "Canva",
        icon: "🎨",
        commission: "Up to 20%",
        slug: "ai-tools-small-business-owners"
    },
    {
        name: "Synthesia",
        icon: "🎬",
        commission: "20% for 12 months",
        slug: "ai-video-tools-creators"
    },
    {
        name: "Speechify",
        icon: "🔊",
        commission: "50% flat",
        slug: "best-ai-writing-tools-2026"
    },
    {
        name: "AdCreative.ai",
        icon: "📊",
        commission: "30% lifetime",
        slug: "ai-tools-small-business-owners"
    }
];

function renderArticles() {
    const grid = document.getElementById('article-grid');
    if (!grid) return;
    grid.innerHTML = ARTICLES.map(a => `
        <article class="article-card" onclick="location.href='/articles/${a.slug}.html'">
            <div class="category">${a.category}</div>
            <h3><a href="/articles/${a.slug}.html">${a.title}</a></h3>
            <p class="excerpt">${a.excerpt}</p>
            <div class="meta">
                <span>${a.date}</span>
                <span>${a.readTime}</span>
            </div>
        </article>
    `).join('');
}

function renderTools() {
    const grid = document.getElementById('tools-grid');
    if (!grid) return;
    grid.innerHTML = TOOLS.map(t => `
        <div class="tool-card" onclick="location.href='/articles/${t.slug}.html'">
            <div class="tool-icon">${t.icon}</div>
            <h3>${t.name}</h3>
            <div class="commission">${t.commission}</div>
            <a href="/articles/${t.slug}.html" class="tool-link">Read review →</a>
        </div>
    `).join('');
}

function renderProducts() {
    const grid = document.getElementById('product-grid');
    if (!grid) return;
    grid.innerHTML = PRODUCTS.map(p => `
        <div class="product-card" onclick="location.href='/products/${p.slug}.html'">
            ${p.image ? `<div class="product-thumb"><img src="${p.image}" alt="${p.title}" loading="lazy"></div>` : ''}
            <div class="category">${p.category}</div>
            <h3><a href="/products/${p.slug}.html">${p.title}</a></h3>
            <p class="excerpt">${p.excerpt}</p>
            <div class="price">${p.price}</div>
            <a href="/products/${p.slug}.html" class="tool-link">View product →</a>
        </div>
    `).join('');
}

document.addEventListener('DOMContentLoaded', () => {
    renderArticles();
    renderTools();
    renderProducts();

    const form = document.getElementById('newsletter-form');
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const input = form.querySelector('input');
            const btn = form.querySelector('button');
            btn.textContent = 'Subscribed! ✓';
            btn.style.background = '#4ade80';
            input.value = '';
            setTimeout(() => { btn.textContent = 'Subscribe Free'; btn.style.background = ''; }, 3000);
        });
    }
});
