# 🐙 GitPulse: Real-Time Command-Line GitHub Activity Monitor

<p align="center">
  <b>A responsive, light-weight command-line interface (CLI) to stream and filter live GitHub user activity events.</b><br>
  Optimised for rapid telemetry, granular event filtering, and elegant terminal rendering.
</p>

---

<h2>📘 Project Overview</h2>

<p>
<b>GitPulse</b> is a terminal-based activity tracking tool engineered to query public event logs directly from the GitHub REST API. This application was built completely from the ground up as a native solution for the <b><a href="https://roadmap.sh/projects/github-user-activity" target="_blank">GitHub User Activity</a></b> challenge on <b>roadmap.sh</b>.
</p>

<p>
The application bypasses heavy, multi-layered interfaces in favour of a strict, one-line CLI syntax. It is engineered with automated screen management, detailed exception handling, and local JSON telemetry recording. By integrating deep-level text rendering, GitPulse offers granular diagnostic visibility into active codebases, allowing developers to track user contributions directly inside their workflow environment.
</p>

---

<h2>⚡ Core Features & Project Enhancements</h2>

<p>
While fulfilling the core specifications of the roadmap.sh project, GitPulse implements several advanced features that elevate it above standard scripts:
</p>

<table width="100%">
  <thead>
    <tr style="background-color: #0d47a1; color: white;">
      <th style="padding: 10px; text-align: left;">Capability</th>
      <th style="padding: 10px; text-align: left;">Standard Requirements</th>
      <th style="padding: 10px; text-align: left;">GitPulse Implementation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Argument Processing</b></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Accept a basic username argument.</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Dual-mode processing</b> supporting full history dumps or specific event type target filters.</td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Telemetry Logging</b></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Fetch and print directly to console.</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Automatic payload preservation</b> caching the raw API transaction directly to <code>response.json</code> before console delivery.</td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Visual Interface</b></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Plain text output streaming.</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Enhanced terminal visuals utilizing <b>Rich color syntax tags</b>, text separation, and automated shell clearing.</td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>String Sanitisation</b></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Standard JSON attribute parsing.</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Surrogate pair text translation</b> to handle complex UTF-16 character encodings inside repository headers.</td>
    </tr>
    <tr>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Error Interception</b></td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;">Basic termination on failure.</td>
      <td style="padding: 8px; border-bottom: 1px solid #ddd;"><b>Graceful UI timed timeouts</b> displaying step-by-step fallback parameters and filter indexes before exiting safely.</td>
    </tr>
  </tbody>
</table>

---

<h2>🧩 Folder Structure</h2>

<pre>
GitPulse/
│
├── github-activity.py   # Main CLI application entry point and logic
├── README.md            # Detailed system documentation
└── response.json        # Cached raw data payload from the latest API transaction
</pre>

---

<h2>🚀 How to Run</h2>

<ol>
  <li>Ensure you have <b>Python 3.8 or above</b> configured on your local workstation.</li>
  <li>Clone or download this repository locally:
    <pre>git clone https://github.com/Sheikh-H/GitPulse.git</pre>
  </li>
  <li>Navigate directly into the project directory:
    <pre>cd GitPulse</pre>
  </li>
  <li>Install the required external terminal formatting package:
    <pre>pip install rich requests</pre>
  </li>
  <li>Execute commands directly using the syntax layouts detailed in the operational manual below.</li>
</ol>

---

<h2>🖥️ Detailed Usage & Command Manual</h2>

<p>
GitPulse runs dynamically based on the exact positional arguments passed to the script during terminal execution.
</p>

<h3>1. Unfiltered Global Streams</h3>
<p>To pull every recent public interaction log recorded on GitHub for a given profile, pass only the target username:</p>
<pre>python github-activity.py [username]</pre>
<i>Example:</i>
<pre>python github-activity.py Sheikh-H</pre>

<h3>2. Granular Activity Filtering</h3>
<p>To narrow down the stream to a precise form of developer activity, append an event type keyword as a secondary parameter:</p>
<pre>python github-activity.py [username] [filter_type]</pre>
<i>Example (To only extract public star registrations):</i>
<pre>python github-activity.py Sheikh-H WatchEvent</pre>
<i>Example (To view code contribution updates):</i>
<pre>python github-activity.py Sheikh-H PushEvent</pre>

<p>⚠️ <b>Note:</b> If an unsupported or invalid filter phrase is provided, the script automatically triggers a diagnostic screen showing all valid parameters before shutting down the active pipeline.</p>

---

<h2>⚙️ Code Architecture & Function Breakdown</h2>

<p>
This section details how the script processes your arguments and tracks active streams under the hood:
</p>

<h3>Data Acquisition & Caching Engine</h3>
<ul>
  <li><code>fetch_request(username)</code>: Constructs the target URL for the GitHub API endpoint. Handles server connectivity using a hard-coded 10-second timeout to prevent terminal locking. Once a successful request completes, it writes the raw data to disk as a styled <code>response.json</code> backup before passing the runtime dictionary object onwards.</li>
</ul>

<h3>Display Maintenance & Fault Defense</h3>
<ul>
  <li><code>clear_screen()</code>: Inspects local system properties to call matching shell commands (<code>cls</code> for Windows-based shells, <code>clear</code> for UNIX/macOS environments), ensuring the terminal remains free of visual clutter.</li>
  <li><code>error_message(*messages)</code>: Accepts dynamic message arguments during a structural failure. Displays each parameter sequentially with step-by-step structural sleep pauses before completely shutting down the operating framework via a clean <code>sys.exit()</code> call.</li>
</ul>

<h3>Stream Formatters</h3>
<ul>
  <li><code>all_activity(username)</code>: Acts as the global telemetry endpoint. Loops natively through the raw transactions list, outputs decorative spacing rails, and renders targeted repository information alongside decoded text fields.</li>
  <li><code>filtered_activity(username, filter)</code>: Evaluates user input against a hard-coded library of 42 distinct GitHub activity types. Valid entries trigger a targeted layout displaying real-time timestamps (sanitised of messy 'T' or 'Z' indicators), specific tracking blocks, and target repository metadata.</li>
</ul>

---

<h2>📂 Local Telemetry Architecture</h2>

<p>
The application saves its network transactions locally to <code>response.json</code>. This allows for quick local debugging and testing without exhausting your hourly public GitHub API call allowance:
</p>

<h3>Sample Data Layout (<code>response.json</code>)</h3>
<pre>
[
  {
    "id": "40294195281",
    "type": "PushEvent",
    "actor": {
      "id": 499550,
      "login": "Sheikh-H"
    },
    "repo": {
      "id": 98132412,
      "name": "Sheikh-H/developer-roadmap"
    },
    "payload": {
      "push_id": 1629519102,
      "size": 3,
      "distinct_size": 3,
      "description": "Community-driven roadmaps, articles and resources for developers."
    },
    "public": true,
    "created_at": "2026-05-23T16:40:12Z"
  }
]
</pre>

---

<h2>🧰 Requirements & Dependencies</h2>

<ul>
  <li><b>Python Runtime:</b> version 3.8 or above.</li>
  <li><b>Internal Standard Modules:</b> <code>os</code>, <code>sys</code>, <code>json</code>, <code>time</code>.</li>
  <li><b>External Integration Libraries:</b> <code>requests</code> (for secure network requests) and <code>rich</code> (for text color rendering layouts).</li>
</ul>

---

<h2>📄 Licence</h2>

<p>
  This project is licensed under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2026 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>

---

## Footnote

<div align="center" style="border: 1px solid green; padding: 10px; border-radius: 5px;">
  <p>🗣️ Feel free to follow, connect, and chat!</p>
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub">
  </a><a class="header-badge" target="_blank" href="https://www.linkedin.com/in/Sheikh-Hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn">
  </a><a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail">
  </a><a class="header-badge" target="_blank" href="https://Sheikh-H.github.io/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio">
  </a>
</div>

<div align="center">
  <a href="https://www.linkedin.com/in/Sheikh-Hussain/" target="_blank">By Sheikh Hussain 💚</a>  
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
