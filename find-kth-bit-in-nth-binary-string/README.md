<h2>1545. Find Kth Bit in Nth Binary String</h2><h3>Medium</h3><hr><div><p>Given two positive integers <code>n</code> and <code>k</code>, the binary string <code>S<sub>n</sub></code> is formed as follows:</p>

<ul>
	<li><code>S<sub>1</sub> = "0"</code></li>
	<li><code>S<sub><span style="font-size: 10.8333px;">i</span></sub> = S<sub><span style="font-size: 10.8333px;">i-1</span></sub> + "1" + reverse(invert(S<sub><span style="font-size: 10.8333px;">i-1</span></sub>))</code> for <code>i &gt; 1</code></li>
</ul>

<p>Where <code>+</code> denotes the concatenation operation, <code>reverse(x)</code> returns the reversed string <font face="monospace">x,</font> and <code>invert(x)</code> inverts all the bits in <font face="monospace">x</font> (0 changes to 1 and 1 changes to 0).</p>

<p>For example, the first 4 strings in the above sequence are:</p>

<ul>
	<li><code>S<sub>1 </sub>= "0"</code></li>
	<li><code>S<sub>2 </sub>= "0<strong>1</strong>1"</code></li>
	<li><code>S<sub>3 </sub>= "011<strong>1</strong>001"</code></li>
	<li><code>S<sub>4</sub> = "0111001<strong>1</strong>0110001"</code></li>
</ul>

<p>Return <em>the</em> <code>k<sup>th</sup></code> <em>bit</em> <em>in</em> <code>S<sub>n</sub></code>. It is guaranteed that <code>k</code> is valid for the given <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "0"
<strong>Explanation: </strong>S<sub>3</sub>&nbsp;is "<strong><u>0</u></strong>111001". The first bit is "0".
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 4, k = 11
<strong>Output:</strong> "1"
<strong>Explanation: </strong>S<sub>4</sub>&nbsp;is "0111001101<strong><u>1</u></strong>0001". The 11th bit is "1".
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> "0"
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> n = 2, k = 3
<strong>Output:</strong> "1"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>n</sup> - 1</code></li>
</ul>
</div>