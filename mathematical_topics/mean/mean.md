## Definição utilizando a função de perda quadrática

$$f(\mu) = \sum_{i=1}^{n}(y_i - \mu)^2$$

$$\mu = \min \sum_{i=1}^{n}(y_i - \mu)^2$$

## Demonstração da média utilizando a perda quadrática

$$\sum_{i=1}^{n}(y_i - \mu)^2 = 2\sum_{i=1}^{n}(y_i - \mu)$$

$$f'(\mu) = 2\sum_{i=1}^{n}(y_i - \mu) \frac{d}{d\mu}(y_i - \mu)$$

$$= 2\sum_{i=1}^{n}(y_i - \mu)(-1)$$

$$= -2\sum_{i=1}^{n}(y_i - \mu)$$

Agora precisamos achar o ponto $\hat{\mu}$ tal que $f'(\hat{\mu}) = 0$

$$f'(\hat{\mu}) = 0$$

$$-2\sum_{i=1}^{n}(y_i - \mu) = 0$$

$$-\sum_{i=1}^{n}y_i + n\mu = 0$$

$$n\hat{\mu} = \sum_{i=1}^{n}y_i$$

$$\hat{\mu} = \frac{\sum_{i=1}^{n}y_i}{n}$$