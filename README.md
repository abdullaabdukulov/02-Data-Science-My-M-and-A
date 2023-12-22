# 02-Data-Science-My-M-and-A


<div class="row">
<div class="col tab-content">
<div class="tab-pane active show" id="subject" role="tabpanel">
<div class="row">
<div class="col-md-12 col-xl-12">
<div class="markdown-body">
<p class="text-muted m-b-15">
</p><h1>My M And A</h1>
<p>Remember to git add &amp;&amp; git commit &amp;&amp; git push each exercise!</p>
<p>We will execute your function with our test(s), please DO NOT PROVIDE ANY TEST(S) in your file</p>
<p>For each exercise, you will have to create a folder and in this folder, you will have additional files that contain your work. Folder names are provided at the beginning of each exercise under <code>submit directory</code> and specific file names for each exercise are also provided at the beginning of each exercise under <code>submit file(s)</code>.</p>
<hr>    
<table>
<thead>
<tr>
<th>My M And A</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Submit directory</td>
<td>.</td>
</tr>
<tr>
<td>Submit files</td>
<td>my_m_and_a.py - my_ds_babel.py</td>
</tr>
</tbody>
</table>
<h3>Description</h3>
<p>You've worked as a <code>Junior Data Engineer</code> at <code>Plastic Free Boutique</code> for three months.</p>
<p>Your first mission was to build a strong, robust, and scalable <code>customers</code> database for the exponential growth the company will soon have. Your manager is delighted.</p>
<p>We've just acquired a new company, <code>Only Wood Box,</code> which will be a perfect solution for our packaging department. They are experts in making wood packages at a competitive, light, and cheap price.</p>
<p>Expert in their technology, they didn't believe in the digital world. Despite the decent number of customers, they didn't have to invest in their infrastructure. Before quitting, their engineer told us that at least we had stored all the information; I don't understand what he meant.</p>
<p>You should use <code>import pandas as pd</code></p>
<p>Your mission will be to merge their three customers (yes 3 :D) table into ours.</p>
<ul>
<li>
<p><a href="https://storage.googleapis.com/qwasar-public/only_wood_customer_us_1.csv" target="_blank">Table 1</a></p>
</li>
<li>
<p><a href="https://storage.googleapis.com/qwasar-public/only_wood_customer_us_2.csv" target="_blank">Table 2</a></p>
</li>
<li>
<p><a href="https://storage.googleapis.com/qwasar-public/only_wood_customer_us_3.csv" target="_blank">Table 3</a></p>
</li>
</ul>
<h2>Technical description</h2>
<p>Our database schema:</p>
<pre class=" language-plain"><code class=" language-plain">"gender" - 'string'
"firstname" - 'string'
"Lastname" - 'string'
"email" - 'string'
"age" - 'string'
"city" - 'string'
"country" - 'string'
"created_at" - 'string'
"referral" - 'string'
</code></pre>
<p>1# Your function will be called <code>my_m_and_a</code> and receive the 3 <code>CSV</code> content.
2# Import your function from my_ds_babel to save the CSV's content into SQL.</p>
<h2>VERY IMPORTANT</h2>
<p>We want to move on after this merge &amp; acquisition; we don't want to keep their <code>.csv</code>; if they are seen in your repository during your 1-1 meeting (Peer Review), it will be considered a fail for this project.</p>
<p><strong>Example00</strong></p>
<pre class=" language-plain"><code class=" language-plain">merged_csv = my_m_and_a(content_database_1, content_database_2, content_database_3)
my_ds_babel.csv_to_sql(merged_csv, 'plastic_free_boutique.sql', 'customers')
</code></pre>
<p><em>Tip</em>
Google: .gitignore file :-)</p>

<p></p>
</div>

</div>
</div>
</div>
<div class="tab-pane" id="resources" role="tabpanel">
</div>
</div>
</div>
