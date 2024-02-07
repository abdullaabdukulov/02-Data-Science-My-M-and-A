# Welcome to My M and A project

## Task
The task is loading `3 datasets` and then we have to clean up them. As well as, creating a dataframe which those cleaned 
datasets should merge. Lastly, convert it into sql(database)

## Description 
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

## Installation
```bash
 pip install -r requirements.txt
```

## Usage
First of all you need to clone this repository.
<br>
Then run the `my_m_and_a.py` using this command below
```bash
  # write it in your terminal
  python my_m_and_a.py
```
After running go to this file and `uncomment` the code line which located in 10th line and
rewrite the name of **`databese`** and **`table_name`** in your case. Then **`rerun`** the code.
