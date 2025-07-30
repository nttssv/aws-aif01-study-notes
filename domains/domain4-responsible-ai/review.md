## Understanding Responsible AI (Task 4.1)
- Understand what **Responsible AI** is and its core principles.
- Identify features of responsible AI systems (e.g., fairness, safety, accountability).
- Know tools that support responsible AI practices.
- Learn how responsible AI affects:
  - Model selection
  - Risk assessment
  - Dataset design and characteristics
- Understand **bias and variance** in responsible AI context.
- Use tools to:
  - Detect bias
  - Monitor model behavior
  - Evaluate trustworthiness and truthfulness



![alt text](../../img/image.png)
![alt text](../../img/Effects-of-bias-and-variance.png)
![alt text](../../img/Pasted-Graphic-4.png)
# Class Imbalance and Its Impact on Model Performance

## What is Class Imbalance?

Class imbalance occurs when a **feature value has significantly fewer training samples** compared to other values in the dataset.

### Example:
- Feature: **Sex**
  - Women: **32.4%** of training data
  - Men: **67.6%** of training data

This imbalance means the model has seen **more data for men** than for women during training.

## Effects on the Model

- **Better Performance on Majority Class (Men):**
  - More data → more representative patterns learned.
- **Risk of Overfitting the Minority Class (Women):**
  - Fewer samples → model may memorize rather than generalize.
- **Higher Error Rate for Women:**
  - Less exposure → poorer predictions.

## Real-World Consequence

If this model is used to **predict diseases**:
- Women may be **misdiagnosed** more often.
- This could lead to **inequity in healthcare outcomes** and mistrust in the model.

---

> ✅ Addressing class imbalance is essential for **fair, robust, and trustworthy AI**.

![alt text](image-1.png)
![alt text](<Pasted Graphic 8.png>)
![alt text](<Pasted Graphic 9.png>)
![alt text](<SageMaker Clarify processing jobs.png>)
![alt text](image-2.png)
![alt text](<Pasted Graphic 12.png>)
![alt text](<Pasted Graphic 13.png>)
![alt text](<Amazon Bedrock Guardrails.png>)
![alt text](<• Model evaluation.png>)

## Task 4.2: Transparency and Explainability in AI Models
- Understand why **transparency and explainability** are key challenges in responsible AI.
- Define what makes a model **transparent** or **explainable**.
- Know tools that support explainability (e.g., SHAP, LIME, SageMaker Clarify).
- Evaluate **tradeoffs** between:
  - Model safety/security
  - Model transparency/explainability
- Understand how **human-centric design** supports better explainability in AI systems.
![alt text](<Model transparency.png>)
![alt text](<Interpretability compared to performance.png>)
![alt text](<Transparency and model safety.png>)
![alt text](<Open source Al models.png>)
![alt text](<Model transparency on AWS.png>)
![alt text](<SageMaker Clarify model explainability.png>)
![alt text](<What is human-centered Al.png>)
![alt text](<Amazon Augmented Al.png>)
![alt text](<Reinforcement learning from human feedback (RLHF).png>)
![alt text](<Amazon SageMaker Ground Truth.png>)