# Portfolio Chatbot and Feature Plan

## Security First

The DeepSeek API key must not be committed to GitHub or exposed in browser code.

Recommended actions:

- Rotate the API key because it was shared in plain text.
- Store the new key in `.env` locally as `DEEPSEEK_API_KEY`.
- Add the same key in Render Dashboard under Environment Variables.
- Keep `.env` ignored by Git.
- Call DeepSeek only from Django backend views or services.

Example environment variables:

```env
DEEPSEEK_API_KEY=your_rotated_key_here
DEEPSEEK_API_URL=https://api.deepseek.com/chat/completions
DEEPSEEK_MODEL=deepseek-v4-flash
```

## Chatbot Goal

Add a portfolio assistant that helps visitors learn about Turja Das, projects, skills, research, CV, and contact options.

The chatbot should feel useful, not like a generic AI widget. It should answer questions such as:

- What projects has Turja built?
- What technologies does Turja use?
- Tell me about the SUMS project.
- Where can I see the live project?
- How can I contact Turja?
- Can I download the CV?
- What research has Turja published?

## Recommended Chatbot Architecture

### Backend

Create a Django endpoint:

```text
POST /api/chat/
```

Suggested request body:

```json
{
  "message": "Tell me about SUMS"
}
```

Suggested response:

```json
{
  "reply": "SUMS is a Smart University Management System..."
}
```

Backend responsibilities:

- Read `DEEPSEEK_API_KEY` from environment variables.
- Build a system prompt using portfolio context.
- Send user message to DeepSeek.
- Return only the assistant reply to the frontend.
- Apply basic rate limiting or session throttling.
- Never expose the API key in HTML, JavaScript, or API responses.

### Portfolio Context

The chatbot should receive a compact context about:

- Name: Turja Das
- Role: Full Stack Developer
- Core stack: Python, Django, PostgreSQL, Docker, DevOps
- Projects from the `Project` model
- Skills from the `Skill` model
- Research paper title and DOI
- Contact email and LinkedIn
- CV download route

Best approach:

- Query live project and skill data from the database.
- Append static profile/research/contact information.
- Keep the prompt short so API cost stays low.

### Frontend

Add a floating chat button near the bottom-right of the site.

Expected UI states:

- Closed floating button
- Open chat panel
- Welcome message
- Message list
- Typing/loading state
- Error state
- Clear chat button
- Mobile-friendly full-width bottom panel

Suggested behavior:

- Do not open automatically.
- Start with quick prompt buttons:
  - `Projects`
  - `Skills`
  - `Research`
  - `Contact`
- Keep chat history in browser memory during the current page session.
- Do not store visitor chats unless a future dashboard feature requires it.

## Implementation Steps

### Phase 1: Safe Backend Setup

1. Add DeepSeek settings to `portfolio/settings/base.py`.
2. Create a Django service file, for example:

```text
core/services/chatbot.py
```

3. Create a chat API view in `core/views.py` or a dedicated `core/api_views.py`.
4. Add a URL route in `core/urls.py`.
5. Return clear errors if the API key is missing.

### Phase 2: Portfolio-Aware Prompt

1. Load projects from `Project.objects.all()`.
2. Load skills from `Skill.objects.all()`.
3. Include research, CV, contact, and social links.
4. Tell the assistant to answer only about the portfolio and professional topics.
5. Tell the assistant to redirect unrelated questions back to portfolio topics.

### Phase 3: Frontend Widget

1. Add chatbot HTML to `core/templates/core/home.html`.
2. Add styles using the existing Tailwind design language.
3. Add JavaScript in the template or a static JS file.
4. Connect the form submit to `/api/chat/`.
5. Add loading and error states.

### Phase 4: Deployment

1. Rotate the DeepSeek API key.
2. Add the new key to local `.env`.
3. Add the new key to Render environment variables.
4. Deploy to Render.
5. Test the live site chatbot from a browser.

### Phase 5: Hardening

1. Add rate limiting.
2. Limit message length.
3. Add CSRF handling.
4. Add timeout handling for DeepSeek requests.
5. Log backend errors without logging API keys or full private messages.

## Suggested System Prompt

```text
You are the portfolio assistant for Turja Das, a full stack developer.
Answer questions about Turja's projects, skills, research, CV, and contact details.
Use the provided portfolio context as your source of truth.
Be concise, friendly, and professional.
If a question is unrelated to Turja's portfolio, politely guide the visitor back to projects, skills, research, or contact.
Never claim Turja has skills, jobs, degrees, or achievements that are not in the context.
```

## Other Features to Add to the Portfolio

### 1. Project Detail Pages

Create one detail page for each project.

Each page can include:

- Problem statement
- Features
- Tech stack
- Screenshots
- GitHub link
- Live link
- Challenges solved
- Future improvements

Why it helps:

Recruiters and clients can understand the depth of each project instead of only seeing cards.

### 2. Project Screenshots or Demo Gallery

Add project images to make the portfolio more visual.

Recommended screenshots:

- SUMS login page
- Student dashboard
- Teacher dashboard
- Admin dashboard
- API or analytics page

Why it helps:

Visual proof makes projects feel more real and polished.

### 3. Case Study for SUMS

Create a featured case study section for the Smart University Management System.

Include:

- 40+ API endpoints
- 3 AI features
- 5 dashboards
- Role-based authentication
- PythonAnywhere live deployment

Why it helps:

SUMS appears to be a strong flagship project, so it deserves a deeper presentation.

### 4. Resume Analytics

Track how often visitors download the CV.

Possible model:

```text
ResumeDownload
- created_at
- ip_hash
- user_agent
```

Why it helps:

You can understand whether visitors are engaging seriously.

### 5. Contact Dashboard Improvements

Improve the dashboard message system.

Ideas:

- Mark messages as replied
- Add priority labels
- Add search/filter
- Add email reply shortcut
- Add message export

Why it helps:

The dashboard becomes a real admin tool, not just a message list.

### 6. Blog or Notes Section

Add short technical posts.

Good topics:

- Building Django REST APIs
- Deploying Django on Render
- Deploying Django on PythonAnywhere
- PostgreSQL tips
- Dockerizing Django
- AI features in SUMS

Why it helps:

Blog posts show communication skill and technical depth.

### 7. Research Page Upgrade

Turn the current research section into a dedicated page.

Include:

- Abstract summary
- Methodology summary
- Key contribution
- PDF link
- DOI link
- Technologies used

Why it helps:

Your research publication is a strong differentiator.

### 8. Skills by Category With Proof

Enhance skills with evidence.

Example:

- Django: used in portfolio and SUMS
- PostgreSQL: used in portfolio database
- Docker: used in deployment setup
- DRF: used in SUMS APIs

Why it helps:

It turns a skills list into credibility.

### 9. Testimonials or Recommendations

Add a section for feedback from teachers, clients, teammates, or collaborators.

Why it helps:

Social proof improves trust.

### 10. Availability and Services Section

Add a section explaining what work you are available for.

Examples:

- Django web apps
- REST API development
- Portfolio and dashboard systems
- Deployment and DevOps setup
- Database-backed admin systems

Why it helps:

Visitors immediately know how to hire you.

## Recommended Priority Order

1. Rotate API key and add secure environment variables.
2. Add chatbot backend endpoint.
3. Add chatbot frontend widget.
4. Add SUMS screenshots and project detail page.
5. Add blog/notes section.
6. Upgrade contact dashboard.
7. Add resume analytics.
8. Add testimonials.

## Success Checklist

- Chatbot works locally.
- Chatbot works on Render.
- API key is not visible in page source.
- API key is not committed to Git.
- Chatbot answers portfolio questions accurately.
- Chatbot refuses unrelated or unsafe requests politely.
- SUMS appears once locally and on Render.
- Portfolio has stronger proof through screenshots, case studies, and project detail pages.
