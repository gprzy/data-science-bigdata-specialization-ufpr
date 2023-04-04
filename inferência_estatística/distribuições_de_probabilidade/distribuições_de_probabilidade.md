## Distribuições discretas

- **Distribuição de Bernoulli**

$$
f(k;p) =
\begin{cases}
1-p & \text{if } k=0\\
p & \text{if } k=1
\end{cases}
\quad 0\leq p\leq 1
$$

- **Distribuição Binomial**

$$
f(k;n,p) = \binom{n}{k} p^k(1-p)^{n-k} \\
\quad 0\leq p\leq 1
$$

- **Distribuição Geométrica**

$$
f(k;p) = (1-p)^{k-1}p \\
\quad 0\leq p\leq 1, k\geq 1
$$

- **Distribuição Hipergeométrica**

$$
f(k;N,n,K) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}} \\
\quad 0\leq k\leq K, N-K\geq n-k, N\geq n
$$

- **Distribuição de Poisson**

$$
f(k;\lambda) = \frac{\lambda^k e^{-\lambda}}{k!} \\
\quad \lambda>0, k\geq 0
$$

## Distribuições contínuas

- **Distribuição Uniforme**

$$
f(x;a,b) =
\begin{cases}
\frac{1}{b-a} & \text{if } a\leq x\leq b\\
0 & \text{otherwise}
\end{cases}
\quad a\leq b
$$

- **Distribuição Exponencial**

$$
f(x;\lambda) =
\begin{cases}
\lambda e^{-\lambda x} & \text{if } x\geq 0\\
0 & \text{if } x<0
\end{cases}
\quad \lambda>0
$$

- **Distribuição Normal**

$$
f(x;\mu,\sigma^2) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

- **Distribuição Qui-quadrado**

$$
f(x;k) =
\begin{cases}
\frac{1}{2^{k/2}\Gamma(k/2)}x^{k/2-1}e^{-x/2} & \text{if } x\geq 0\\
0 & \text{if } x<0
\end{cases}
\quad k>0
$$

- **Distribuição t de Student**

$$
f(x;k) = \frac{\Gamma\left(\frac{k+1}{2}\right)}{\sqrt{k\pi}\,\Gamma\left(\frac{k}{2}\right)}\left(1+\frac{x^2}{k}\right)^{-\frac{k+1}{2}} \\
\quad k>0
$$