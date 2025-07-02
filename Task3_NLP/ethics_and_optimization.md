## Ethical Considerations

### Bias in MNIST Classifier

The MNIST digit classifier may inherit biases from the dataset itself:

- Digits may have been written by a limited demographic (e.g., age, nationality, handwriting style).
- The model may generalize poorly to digits written by people with different writing styles.
- It might perform worse on certain groups, reducing fairness in practical use.

****Mitigation:******

- Collect a more diverse set of digit samples from different populations.
- Use tools like TensorFlow Fairness Indicators to analyze performance gaps across groups.
- Retrain or fine-tune the model using balanced or augmented data.





### Bias in Amazon Reviews Sentiment / NER

The NLP pipeline on Amazon reviews faces these risks:

- Reviews may reflect societal biases (e.g., more positive/negative language for certain brands).
- Rule-based sentiment analysis may misclassify nuanced or sarcastic text.
- Named Entity Recognition (NER) may miss brand/product names if the training data underrepresents them.

**Mitigation:**

- Expand and diversify training data for NER to include varied brand/product mentions.
- Use spaCy’s rule-based matching to add custom patterns for underrepresented entities.
- For sentiment analysis, supplement rules with data-driven approaches, e.g., fine-tuned classifiers on balanced labeled datasets.

---

### Tools to Mitigate Bias

**TensorFlow Fairness Indicators**:

- Evaluate model performance across slices (e.g., age groups, handwriting styles).
- Highlight disparities in metrics such as accuracy or false positives.

**spaCy Rule-based Systems**:

- Add custom patterns to improve entity recognition for marginalized or underrepresented brands.
- Ensure consistent treatment across product types by making rules explicit.
