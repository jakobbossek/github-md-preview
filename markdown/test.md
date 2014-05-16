# Test file

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet,
consetetur sadipscing elitr, sed **diam nonumy eirmod tempor invidunt** ut labore et
dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo
duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est
Lorem ipsum dolor sit amet.

```splus
library(soobench)
x = sapply(1:10, function(x) x^2 + cos(x))
```

Some more text with and another code block:

```python
import os
def fac(n):
  f = 1
  while (n > 0):
    f = f * n
    n = n - 1
  return f
```

Another code block without explicit language
```
library(soobench)
fn = generate_ackley_function(2)
plot(fn)
```
