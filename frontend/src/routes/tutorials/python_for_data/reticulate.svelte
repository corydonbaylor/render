<script>
  import TutorialLayout from "./tutorials_layout.svelte";
</script>

<TutorialLayout>
  <h1 id="oh-how-i-will-miss-the-tidyverse">Python and R Studio</h1>

  <p>
    There is no better place to write code than R Studio. At least scripting
    code. I think its an objective fact not an opinion that it is better than
    juptyer notebook. First, it allows you to view the data in the environment.
    Second, it allows you to run whatever line of code you want and you get view
    the results in the console. Finally, it also allows you to access to the
    terminal.
  </p>
  <p>
    It works natively with R but the good folks at R Studio have now made it
    work with Python.
  </p>
  <h3>Install <code>reticulate</code> and packages</h3>
  <p>
    First things first, we need to install <code>reticulate</code>. We won&#39;t
    be busting out the <code>pip</code> installer for this one.
    <code>reticulate</code>
    is an R package that makes it possible to use python in R Studio. If you don&#39;t
    have python installed on your computer, install it first. If you do, let&#39;s
    install <code>reticulate</code>:
  </p>
  <pre><code class="language-r" lang="r"
      >install.packages(&quot;reticulate&quot;)
    </code></pre>
  <p>Next, create a python script and trying running something in python:</p>
  <pre><code class="language-python" lang="python"
      >print(&quot;hello world&quot;)
    </code></pre>
  <p>
    How good would python really be if you couldn&#39;t use packages. Installing
    python packages will oddly be done in R not in python. So back over to the R
    side of things:
  </p>
  <pre><code class="language-r" lang="r"
      >library(reticulate)
    py_install(&quot;pandas&quot;)
    </code></pre>
  <p>
    Once you run this, it will ask if you want to create a default python
    environment. Answer yes and it will create a <code>venv</code> environment
    called <code>r-reticulate</code>. R Studio will automatically install python
    packages into this environment when you run <code>py_install()</code>
  </p>
  <p>
    Ok, now you have installed pandas into that environment. Next you need to
    make sure that environment is being used by python. In order to do this, go
    to <strong>&quot;Tools &gt;&gt; Global Options &gt;&gt; Python&quot;</strong
    > and then &quot;Python Interpreter&quot;. Then select the version of python
    created by R Studio.
  </p>
  <p>It should be something like this:</p>
  <pre><code
      >~/.virtualenvs/r-reticulate/bin/python
    </code></pre>
  <p>
    Now, lets try loading the <code>pandas</code> package in our python script:
  </p>
  <pre><code
      >import pandas as pd
    </code></pre>
  <p>And boom, it works!</p>
  <h3>Creating a Different <code>venv</code></h3>
  <p>
    Python is a total mess at package management. Unlike in R where you have the
    CRAN repository, you often will find yourself in package management hell. Or
    at least, I do.
  </p>
  <p>
    So in many cases, it may make sense to create a separate <code>venv</code> for
    a given project. In this instance, we are going to create one for web scrapping.
  </p>
  <p>First, in an R script, do the following:</p>
  <pre><code class="language-r" lang="r"
      >library(reticulate)
    
    # create a new environment 
    virtualenv_create(&quot;webscraping&quot;)
    
    # install beautiful soup
    virtualenv_install(&quot;webscraping&quot;, &quot;beautifulsoup4&quot;)
    </code></pre>
  <p>
    This will create a <code>venv</code> called <code>webscraping</code> and
    then install <code>beautifulsoup4</code> into it.
  </p>
  <p>
    I have found that the easiest way to switch to that <code>venv</code> is to
    go to
    <strong>&quot;Tools &gt;&gt; Global Options &gt;&gt; Python&quot;</strong>
    and then select the python interpreter that uses the
    <code>webscraping</code> virtual environment.
  </p>
  <p>
    And now, once we have switched the <code>venv</code>, we can test if our
    package loaded correctly like so:
  </p>
  <pre><code class="language-python" lang="python"
      >from bs4 import BeautifulSoup
    </code></pre>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
</TutorialLayout>
