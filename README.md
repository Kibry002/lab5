<h1>Bookstore API</h1>
<h1>REG-NO: - C027-01-2798/2024</h1>

<h2>What it does</h2>
<p>
This is a simple backend API for managing a bookstore. It allows you to create, view, update, and delete books stored in a PostgreSQL database.
</p>

<h2>Endpoints</h2>
<ul>
  <li><strong>GET /books</strong> – Get all books</li>
  <li><strong>GET /books/{id}</strong> – Get a single book</li>
  <li><strong>POST /books</strong> – Create a new book</li>
  <li><strong>PUT /books/{id}</strong> – Update a book</li>
  <li><strong>DELETE /books/{id}</strong> – Delete a book</li>
</ul>

<h2>How to install and run</h2>

<p><strong>1. Clone the project</strong></p>
<pre><code>git clone &lt;your-repo-url&gt;
cd &lt;your-project-folder&gt;
</code></pre>

<p><strong>2. Create and activate a virtual environment</strong></p>
<pre><code>python -m venv .venv
source .venv/bin/activate   <!-- Mac/Linux -->
.venv\Scripts\activate      <!-- Windows -->
</code></pre>

<p><strong>3. Install dependencies</strong></p>
<pre><code>pip install -r requirements.txt
</code></pre>

<p><strong>4. Start the database</strong></p>
<pre><code>docker-compose up
</code></pre>

<p><strong>5. Set environment variable</strong></p>
<pre><code>DATABASE_URL=postgresql://postgres:postgres@localhost:5432/bookstore_db
</code></pre>

<p><strong>6. Run the app</strong></p>
<pre><code>uvicorn main:app --reload
</code></pre>

<p>
API runs at: http://127.0.0.1:8000<br />
Docs: http://127.0.0.1:8000/docs
</p>