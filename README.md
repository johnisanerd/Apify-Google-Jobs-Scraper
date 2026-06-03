# 💼 Google Jobs API: Job Listings in Clean JSON

> The most efficient, reliable, and developer-friendly way to use the Google Jobs API.

**Actor page:** [apify.com/johnvc/Google-Jobs-Scraper](https://apify.com/johnvc/Google-Jobs-Scraper?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/Google-Jobs-Scraper/input-schema](https://apify.com/johnvc/Google-Jobs-Scraper/input-schema?fpr=9n7kx3)

The Google Jobs API searches Google Jobs and returns clean, structured JSON, one record per listing. Each job includes title, company, location, source platform, the full description, structured highlights (qualifications, responsibilities, benefits), parsed metadata (posting date, schedule type, benefits), and direct apply links across platforms (LinkedIn, Indeed, company site, and more). Supports location targeting, location-radius search, country and language filtering, and pagination.

> Looking for per-result pricing instead of per-page? See the [pay-per-result edition](https://apify.com/johnvc/google-jobs-scraper---pay-per-result?fpr=9n7kx3).

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Google-Jobs-Scraper.git
   cd Apify-Google-Jobs-Scraper
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python google-jobs-search-scraper.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python google-jobs-search-scraper.py
```

## Why Use This Google Jobs API?

**One record per job, fully detailed.** Every listing comes with title, company, location, source, the full description, structured highlights, and parsed metadata, so you can load it straight into an ATS, a dashboard, or an analysis pipeline.

**Direct apply links.** Each job includes apply options across platforms (LinkedIn, Indeed, the company careers site, and more) with direct URLs.

**Targeted search.** Filter by location, country, language, and Google domain, and use location-radius search to focus on a specific area.

**Predictable, pay-per-use pricing.** Billing is per page processed, with no subscription. You control cost with the page limit.

**Easy to automate.** Call it from Python in a few lines, or load it as an MCP tool so assistants like Claude and Cursor can search jobs for you on demand.

## Features

### Core Capabilities
- **Job search** with location, country, language, and Google-domain targeting
- **Location-radius search** to focus results on a specific area
- **Pagination control** with a configurable page cap
- **Direct apply links** across multiple platforms per job
- **Structured highlights**: qualifications, responsibilities, benefits

### Data Quality
- **One record per job** with a stable structure
- **Full description text** plus parsed metadata (posting date, schedule type, benefits)
- **Apply options** with platform names and direct URLs
- **Search metadata** echoed on every record
- **Consistent JSON** shape across every query

## Usage Examples

### Basic search
```json
{
  "query": "Software Engineer",
  "location": "San Francisco, CA",
  "max_pagination": 1
}
```

### Localized search with radius
```json
{
  "query": "Data Scientist",
  "location": "Berlin, Germany",
  "country": "de",
  "language": "de",
  "include_lrad": true,
  "lrad_value": "10",
  "max_pagination": 1
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `string` | Yes | - | Job search query, e.g. `Software Engineer`, `Data Scientist`. |
| `location` | `string` | No | - | Job location (city level recommended), e.g. `San Francisco, CA`. |
| `country` | `string` | No | (none) | Country code (ISO 3166-1 alpha-2), e.g. `us`, `de`. |
| `language` | `string` | No | (none) | Language code for results, e.g. `en`. |
| `google_domain` | `string` | No | `google.com` | Google domain to search. |
| `num_results` | `integer` | No | `100` | Maximum number of job results to return. |
| `max_pagination` | `integer` | No | `0` | Maximum pages to fetch (~10 results each); `0` = unlimited. Each page is billed separately. |
| `include_lrad` | `boolean` | No | `false` | Enable location-radius filtering. |
| `lrad_value` | `string` | No | `5` | Radius in km when `include_lrad` is true. |
| `output_file` | `string` | No | - | Optional filename to save results. |

## Output Format

A real result for `Software Engineer` in San Francisco (one item per job; the full `description`, `job_highlights`, `extensions`, and `detected_extensions` are present but omitted here for readability, and `job_id` is truncated).

```json
{
  "title": "Software Engineer",
  "company_name": "Lockheed Martin",
  "location": "San Francisco, CA",
  "via": "Lockheed Martin Careers",
  "apply_options": [
    {
      "title": "Lockheed Martin Careers",
      "link": "https://www.lockheedmartinjobs.com/job/owego/software-engineer/694/93796107616"
    }
  ],
  "job_id": "eyJqb2JfdGl0bGUiOiJTb2Z0d2FyZSBFbmdpbmVlciIsImNvbXBhbnlfbmFtZSI6...",
  "query": "Software Engineer",
  "country": "us",
  "language": "en",
  "google_domain": "google.com",
  "search_timestamp": "2026-05-29T11:10:36",
  "total_jobs_found": 10,
  "pages_processed": 1
}
```

Each job record also includes the full `description` text, a `job_highlights` array (qualifications, responsibilities, benefits), an `extensions` array of raw tags (for example `Full-time`), and a `detected_extensions` object with parsed fields like posting date and schedule type.

---

## Use as an MCP tool

You can load the Google Jobs API as an MCP tool so assistants call it for you. The MCP server URL preloads just this one Actor:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper
```

Authenticate with OAuth in the browser when offered, or with your Apify API token (the same `APIFY_API_TOKEN` used by the Python example). Get a token at https://console.apify.com/settings/integrations and a free Apify account at https://apify.com?fpr=9n7kx3 .

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the Google Jobs API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the Google Jobs API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the Google Jobs API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/Google-Jobs-Scraper`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper`, using OAuth when prompted.
5. Ask Claude to run the Google Jobs API.

Open Claude on the web: https://claude.ai

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the Google Jobs API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/Google-Jobs-Scraper`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the Google Jobs API to power recruiting tools, market research, and analytics with reliable, structured results.*

Last Updated: 2026.06.04
