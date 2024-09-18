# Language Complexity

A python package to compute typology-oriented information-based language complexity metrics from written text samples, using compression algorithms.

## Example Usage

```python
from lang_complexity.complexity import complexities
metric = complexities["morphology_deletion_gzip"]
metric.compute("This is only a sample text.")
```
## References
This repository is based in the following papers:

- Juola, P. (2008). Assessing linguistic complexity. Language Complexity: Typology, Contact, Change. John Benjamins Press, Amsterdam, Netherlands.
- Ehret, K., & Szmrecsanyi, B. (2016). An information-theoretic approach to assess linguistic complexity. In Complexity, Isolation, and Variation (pp. 71–94). https://doi.org/10.1515/9783110348965-004
- Serras, F., Carpi, M., Branco, M., & Finger, M. (2024, August). Analysing and Validating Language Complexity Metrics Across South American Indigenous Languages. In Proceedings of the Workshop on Cognitive Modeling and Computational Linguistics (pp. 152-165).

