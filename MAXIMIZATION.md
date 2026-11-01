# AI Level Up — Maximization Field Guide

Reference for the `Maximization` command. It helps the game master audit which features of the player's AI app they use, and which ones would pay off next.

Add this file as a knowledge file (in a Custom GPT, Claude Project, Gemini Gem or Perplexity Space) for a sharper audit. The game works without it.

> **Feature names and plan availability change often.** This guide is a starting map, not a source of truth. Confirm each feature against what the player can actually see in their app before recommending it, and say which plan it needs when you aren't sure.

---

## The 10 feature areas

| # | Area | What it does for the player | First move |
|---|---|---|---|
| 1 | **Customization & memory** | The AI knows who you are, how you work and how you like answers, without being told each time. | Write custom instructions: your role, audience, preferred format, things to avoid. |
| 2 | **Projects & workspaces** | Keeps the files, instructions and chats for one project together. | Make one workspace for your most active project and move its files in. |
| 3 | **Skills, GPTs & Gems** | A saved assistant for a task you repeat, which others can use too. | Turn your most-used prompt into a custom assistant. |
| 4 | **Files & knowledge** | The AI works from your documents instead of general knowledge. | Upload the 3 documents you reference most. |
| 5 | **Plug-ins & connectors** | The AI reads from and acts in your email, calendar, drive and other apps. | Connect one app you open every day. |
| 6 | **Deep research** | Multi-step research with sources, in minutes. | Run one research report on a real decision you face this week. |
| 7 | **Creation tools** | Edit documents and code side by side; generate images, video, slides, files. | Draft your next deliverable in the canvas or artifact view instead of plain chat. |
| 8 | **Voice & vision** | Talk instead of type; show the AI your camera or screen. | Do your next brainstorm in voice mode, out loud. |
| 9 | **Automation & agents** | Scheduled tasks, and agents that take actions for you. | Schedule one recurring briefing or check-in. |
| 10 | **Code & data** | Analyze spreadsheets, run code, build small tools without coding knowledge. | Upload a spreadsheet and ask for the three most useful insights and a chart. |

---

## Platform map

Where each area usually lives. These are the feature names as of late 2026; check the app.

### ChatGPT (OpenAI)
1. Custom instructions · Memory
2. Projects
3. Custom GPTs
4. File uploads · Project files · GPT knowledge
5. Connectors / apps (Gmail, Google Drive, Calendar and others)
6. Deep research
7. Canvas · image generation · Sora video
8. Voice mode · camera and screen sharing on mobile
9. Tasks (scheduled) · Agent mode
10. Data analysis · Codex

### Claude (Anthropic)
1. Profile preferences · Styles · Memory
2. Projects
3. Skills
4. Project knowledge · file uploads
5. Connectors (Gmail, Google Calendar, Drive and others, plus custom MCP connectors)
6. Research
7. Artifacts · file creation (documents, spreadsheets, slides)
8. Voice mode
9. Claude in Chrome · Claude Code · scheduled tasks where available
10. Analysis and code execution · Claude Code

### Gemini (Google)
1. Saved info · personal context
2. Gems · NotebookLM notebooks
3. Gems
4. File uploads · Google Drive
5. Apps (Gmail, Drive, Docs, Calendar, Maps, YouTube) · Gemini in Workspace
6. Deep Research
7. Canvas · image generation · Veo video
8. Gemini Live (camera and screen)
9. Scheduled actions · Agent mode
10. Code execution · Gemini in Sheets · Colab

### Microsoft Copilot
1. Memory · personalization
2. Notebooks · Pages
3. Agents (Copilot Studio, on work plans)
4. File uploads · OneDrive and SharePoint (work plans)
5. Copilot inside Word, Excel, PowerPoint, Outlook and Teams (Microsoft 365 plans)
6. Researcher (work plans) · Think Deeper
7. Pages · image generation
8. Copilot Voice · Copilot Vision
9. Agents · Copilot Actions
10. Copilot in Excel · Python in Excel

### Grok (xAI)
1. Custom instructions · memory
2. Projects
3. Custom instructions per project
4. File uploads
5. Real-time X (Twitter) search
6. DeepSearch
7. Grok Imagine (image and video)
8. Voice mode
9. Tasks (scheduled)
10. Code execution in chat

### Perplexity
1. Profile and preferences
2. Spaces
3. Spaces with custom instructions
4. Space files · file uploads
5. Connectors (Google Drive and others) · Comet browser
6. Research mode
7. Labs (reports, dashboards, small apps)
8. Voice mode
9. Tasks (scheduled) · Comet browser agent
10. Labs

### Open and local models (Llama, Mistral, Qwen, DeepSeek and others, through LM Studio, Ollama, Open WebUI and similar)
1. System prompt
2. Saved chats or workspaces in your app
3. Saved model presets or system prompts
4. Local document chat (RAG)
5. Tool and MCP support in apps that offer it
6. Web search plugins
7. Varies by app
8. Speech-to-text and text-to-speech add-ons
9. Scripts and automation tools (n8n and similar)
10. Run models privately on your own machine. Use it for sensitive data.

---

## Running the audit

1. **Confirm the app and plan.** Ask if it isn't obvious. Free and paid plans differ a lot.
2. **Walk through the 10 areas quickly.** Ask yes or no: "Do you use X?" Mark each area In use, Unused, or Not on this plan.
3. **Score coverage** = In use ÷ available on their plan (for example 6/10, or 5/8 on a free plan).
4. **Pick the top 3 unused areas by payoff for this player's real projects.** Not by novelty. A podcaster gets more from voice and file features than from code execution.
5. **For each, give** what it is in one line, why it matters for their project, a 5-minute setup step, and a Daily Quest (+20 XP). Adopting it (3 real uses) pays +50 XP.
6. **Feed the skill trees.** Plug-ins, connectors, automation and agents count as evidence for Connecting Tools. Customization, memory, projects and skills count for Context & Personalization. A Mirror Test after setting up memory shows whether it worked. An unused feature is never a penalty, only an opportunity.

### Example output

```
─ MAXIMIZATION SCAN // ChatGPT Plus ───────────────
 COVERAGE  █████░░░░░ 5/10
 IN USE    Memory · Projects · Canvas · Voice · Uploads
 TOP 3 UNLOCKS
 1. Plug-ins & connectors → link Google Drive so your client briefs are one prompt away.
    Setup: Settings → Connectors → Google Drive.  D-quest +20 · adopted +50
 2. Tasks → a Monday 8am content-ideas briefing for your newsletter.
 3. Skills, GPTs & Gems → a Custom GPT to turn your "rewrite in my voice" prompt into one your VA can use.
───────────────────────────────────────────────────
```
