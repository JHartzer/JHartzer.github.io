---
layout: post
title: Include Data with your Papers
author: Jacob Hartzer
date: 2025-03-07
description:
tags: LaTeX
categories:
related_posts: false
---

You should include your plotting code **and the data** in your papers and reports. Far too often, I have included a figure in a paper I am writing and after the fact changed my mind about how the data should be presented. Often these are trivial things like colors, styles, and sizes. But sometimes, I want to augment or remove entire lines within the plots. Obviously this is not easy to fix if you have to go back and forth between your code that generates the plot and your paper, constantly copying files from one to the other. Or, even worse, what if you deleted your data or the script used to generate your plots?

This problem can therefore range from small to quite large headaches. When dealing with submission deadlines, it's best to avoid these issues altogether by including your plotting code and data in your repository where you keep your paper.

What's that? You don't keep your paper in its own repository?
1. Put your paper in a repository (because you're obviously using LaTeX)
2. Put your plot generation scripts and data into that repository

Now obviously you shouldn't put **all** your data in the repository, because that would be quite untenable for some things. So it is best to pare it down to the data you would like to plot. Typically I don't even separate the data from the plotting script, opting to save the data within the python plotting script itself, like the following

```python
#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt

# Save your data in the file
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
y = np.array([2,4,1,3,5,2,4,1,3,5,2,4,1,3,5])

plt.plot(x, y)

plt.xlabel('Time [s]')
plt.ylabel('Distance [m]')

plt.title('Example Plot')

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'Example.pdf')
plt.savefig(filename)
```

Additionally, since you have all the information you need to generate the plots using the committed script, it is not necessary to add the figures themselves to git. This can slightly reduce repo size. I typically combine these scripts with my [LaTeX preprocessor]({% post_url 2023-12-12-svg-preprocessor %}) to ensure everything is up-to-date.
