# 📡 GitHub Activity Monitor CLI

<p align="center">
  <b>A lightweight command-line interface for monitoring, filtering, and analysing GitHub user activity events.</b><br>
  Built for API interaction, terminal-based telemetry, and structured developer activity tracking using Python.
</p>

---

<h2>📘 Project Overview</h2>

<p>
<b>GitHub Activity Monitor CLI</b> is a terminal-based monitoring application developed in Python that retrieves and processes public GitHub activity events through the GitHub REST API.
</p>

<p>
This project was created as part of the <b><a href="https://roadmap.sh/projects/github-user-activity" target="_blank">GitHub User Activity</a></b> challenge on <b>roadmap.sh</b>. The purpose of the project is to demonstrate practical understanding of API requests, JSON data processing, command-line applications, and external data handling.
</p>

<p>
The application allows users to monitor recent GitHub events for any public GitHub profile directly from the terminal. Users can retrieve complete activity streams or filter results by specific GitHub event types, providing a lightweight alternative to browser-based activity dashboards.
</p>

<p>
Instead of relying on graphical interfaces, the system follows a direct CLI workflow where users provide a GitHub username and optional filtering parameters. The application communicates with GitHub's public API, processes the returned JSON payload, and renders meaningful activity information directly inside the terminal.
</p>

---

<h2>🧠 Architectural Philosophy & Design Intent</h2>

<p>
The project was intentionally designed around a transparent API processing pipeline:
</p>

<pre>
GitHub API Request
        ↓
Raw JSON Response
        ↓
Local response.json Storage
        ↓
JSON Parsing
        ↓
Terminal Rendering
</pre>

<p>
The application saves the original API response before processing any information. This design choice was implemented to strengthen understanding of:
</p>

<ul>
  <li>HTTP request handling.</li>
  <li>JSON serialisation and deserialisation.</li>
  <li>File persistence workflows.</li>
  <li>External API data structures.</li>
  <li>Transforming raw API responses into readable output.</li>
</ul>

<p>
By preserving the original response payload, developers can inspect the exact JSON returned from GitHub and compare it against the processed terminal output.
</p>

---

<h2>⚡ Core Features</h2>

<ul>
  <li>Retrieve public GitHub user activity through the GitHub REST API.</li>
  <li>Display recent repository activity directly inside the terminal.</li>
  <li>Filter events using specific GitHub event types.</li>
  <li>Automatically cache API responses locally.</li>
  <li>Handle invalid usernames and API failures gracefully.</li>
  <li>Clean terminal interface with structured output formatting.</li>
  <li>Cross-platform terminal clearing support.</li>
  <li>Readable timestamp formatting.</li>
  <li>Repository and event metadata extraction.</li>
</ul>

---

<h2>📊 Supported Activity Filtering</h2>

<p>
The application supports filtering GitHub activity using GitHub's public event categories.
</p>

<table width="100%">
<thead>
<tr>
<th>Event Type</th>
<th>Description</th>
</tr>
</thead>

<tbody>
<tr>
<td><code>PushEvent</code></td>
<td>Displays repository code pushes and commits.</td>
</tr>

<tr>
<td><code>WatchEvent</code></td>
<td>Displays repository starring activity.</td>
</tr>

<tr>
<td><code>CreateEvent</code></td>
<td>Displays repository, branch, or tag creation.</td>
</tr>

<tr>
<td><code>IssuesEvent</code></td>
<td>Displays issue activity.</td>
</tr>

<tr>
<td><code>PullRequestEvent</code></td>
<td>Displays pull request activity.</td>
</tr>

<tr>
<td><code>ForkEvent</code></td>
<td>Displays repository fork activity.</td>
</tr>
</tbody>
</table>

---

<h2>🧩 Folder Structure</h2>

<pre>
Github-Activity-Monitor-CLI/

│
├── github-activity.py   # Main CLI application and API processing logic
├── response.json        # Cached GitHub API response data
└── README.md            # Project documentation
</pre>

---

<h2>🚀 How to Run</h2>

<ol>

<li>
Ensure Python <b>3.8+</b> is installed.
</li>

<li>
Clone the repository:
<pre>
git clone https://github.com/Sheikh-H/Github-Activity-Monitor-CLI.git
</pre>
</li>

<li>
Navigate into the project directory:
<pre>
cd Github-Activity-Monitor-CLI
</pre>
</li>

<li>
Install required dependencies:
<pre>
pip install requests rich
</pre>
</li>

<li>
Run the application:
</li>

</ol>

<pre>
python github-activity.py [username]
</pre>

Example:

<pre>
python github-activity.py Sheikh-H
</pre>

---

<h2>🖥️ Usage Guide</h2>

<h3>1. Display All User Activity</h3>

<p>
Retrieve all recent public GitHub activity events:
</p>

<pre>
python github-activity.py Sheikh-H
</pre>


<h3>2. Filter Specific Activity Types</h3>

<p>
Retrieve only a specific event category:
</p>

<pre>
python github-activity.py Sheikh-H PushEvent
</pre>

Example:

<pre>
python github-activity.py Sheikh-H WatchEvent
</pre>

<p>
If an invalid event type is provided, the application displays available filtering options before exiting safely.
</p>

---

<h2>⚙️ Code Architecture</h2>

<p>
The application is divided into several functional layers responsible for API communication, processing, validation, and presentation.
</p>

---

<h3>🌐 API Communication Layer</h3>

<ul>

<li>
<b><code>fetch_request(username)</code></b>

<p>
Responsible for communicating with the GitHub REST API.
</p>

Handles:

<ul>
<li>API URL construction.</li>
<li>Network requests.</li>
<li>Timeout protection.</li>
<li>Error handling.</li>
<li>Saving raw JSON responses.</li>
</ul>

</li>

</ul>

---

<h3>💾 Local Data Storage</h3>

<ul>

<li>
<b><code>response.json</code></b>

<p>
Stores the latest API response locally for debugging, inspection, and learning purposes.
</p>

</li>

</ul>

---

<h3>🖥️ Terminal Interface Layer</h3>

<ul>

<li>
<b><code>clear_screen()</code></b>

<p>
Automatically clears the terminal depending on the operating system.
</p>

Supports:

<ul>
<li>Windows (<code>cls</code>)</li>
<li>Linux/macOS (<code>clear</code>)</li>
</ul>

</li>


<li>
<b><code>error_message()</code></b>

<p>
Provides structured error output before safely terminating execution.
</p>

</li>

</ul>

---

<h3>📡 Activity Processing</h3>

<ul>

<li>
<b><code>all_activity(username)</code></b>

<p>
Processes and displays the complete GitHub activity history.
</p>

</li>


<li>
<b><code>filtered_activity(username, filter)</code></b>

<p>
Processes only matching GitHub event types and formats the information into readable terminal output.
</p>

</li>

</ul>

---

<h2>📂 Local API Data Architecture</h2>

<p>
The application stores the latest GitHub API response inside <code>response.json</code>.
</p>

Example:

<pre>
[
 {
   "id": "40294195281",
   "type": "PushEvent",
   "actor": {
      "login": "Sheikh-H"
   },
   "repo": {
      "name": "example-project"
   },
   "created_at": "2026-05-23T16:40:12Z"
 }
]
</pre>

<p>
The stored response allows developers to inspect the original API structure and understand how GitHub represents user activity.
</p>

---

<h2>🧪 Error Handling & Validation</h2>

<p>
The application includes defensive programming techniques to prevent unexpected failures.
</p>

<ul>
<li>Handles invalid usernames.</li>
<li>Handles failed API requests.</li>
<li>Validates event filters.</li>
<li>Prevents application crashes from malformed responses.</li>
<li>Uses controlled application shutdowns.</li>
</ul>

---

<h2>🧰 Requirements & Dependencies</h2>

<ul>

<li>
<b>Python:</b> Version 3.8 or above
</li>

<li>
<b>Standard Libraries:</b>

<code>
os
sys
json
time
</code>

</li>

<li>
<b>External Libraries:</b>

<ul>
<li><code>requests</code> - HTTP API communication</li>
<li><code>rich</code> - Enhanced terminal rendering</li>
</ul>

</li>

</ul>

---

## 📄 Licence

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
  <a class="header-badge" target="_blank" href="https://github.com/Sheikh-H"><img src="https://img.shields.io/badge/GitHub-376e00?style=flat&logo=github&logoColor=white" alt="GitHub"></a>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/sheikh-hussain/"><img src="https://img.shields.io/badge/LinkedIn-376e00?style=flat&logo=LinkedIn&logoColor=white" alt="LinkedIn"></a>
  <a class="header-badge" target="_blank" href="mailto:sheikh.hussain1155@gmail.com"><img src="https://img.shields.io/badge/Gmail-376e00?style=flat&logo=gmail&logoColor=white" alt="Gmail"></a>
  <a class="header-badge" target="_blank" href="https://sheikh-hussain.onrender.com/"><img src="https://img.shields.io/badge/Portfolio-376e00?style=flat&logo=github&logoColor=white" alt="Portfolio"></a>
</div>

<div align="center">
  <a href="https://sheikh-hussain.onrender.com/" target="_blank">By Sheikh Hussain 💚</a>
</div>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>


---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>
