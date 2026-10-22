# K = K_chain ⊗ K_tree — Complete Fermion Mass Derivation (Part 2)

## 3.2 Dirac Pairing and Coxeter Outer Automorphism

The K-chain satisfies complementary pairing:

$$n \leftrightarrow N_d - n = 44 - n$$

Eigenvalues satisfy:

$$\gamma_n + \gamma_{44-n} = 4$$

**Proof**:
$$\gamma_n + \gamma_{44-n} = 4\sin^2(\pi n/88) + 4\sin^2(\pi(44-n)/88)$$
$$= 4\sin^2(\pi n/88) + 4\cos^2(\pi n/88) = 4$$

This corresponds to the **outer automorphism** of the Coxeter group $A_{87}$ (the Dynkin diagram with 87 nodes). The reflection symmetry $n \leftrightarrow 88-n$ of the $A_{87}$ diagram produces this pairing. Physically, this corresponds to chiral symmetry or particle-hole symmetry.

**Theorem 2 (Dirac Pairing)**: The complementary pairing $n \leftrightarrow 44-n$ generates a Dirac 2-component spinor structure $\Psi_n = (\varphi_n, \varphi_{44-n})^T$ with:

$$\gamma_n + \gamma_{44-n} = 4 = B = \varphi^3 - \varphi^{-3}$$

This is the branching factor of the MERA (Multi-scale Entanglement Renormalization Ansatz) tensor network.

### 3.3 Numerical Verification

$$\gamma_1 + \gamma_{43} = 0.005096 + 3.994904 = 4.000000 \checkmark$$
$$\gamma_4 + \gamma_{40} = 0.081014 + 3.918986 = 4.000000 \checkmark$$
$$\gamma_5 + \gamma_{39} = 0.126101 + 3.873899 = 4.000000 \checkmark$$
$$\gamma_6 + \gamma_{38} = 0.180736 + 3.819264 = 4.000000 \checkmark$$
$$\gamma_8 + \gamma_{36} = 0.317493 + 3.682507 = 4.000000 \checkmark$$
$$\gamma_9 + \gamma_{35} = 0.398918 + 3.601082 = 4.000000 \checkmark$$

All six active modes confirmed.

---

## 4. Z₂ Grading: Lucas Parity Selection Rule

### 4.1 Binet Formula Parity

The Lucas numbers have a closed form via the Binet formula:

$$L_n = \varphi^n + (-\varphi)^{-n}$$

For different $n$ parity:

- **$n$ even** ($n = 2k$): $(-\varphi)^{-n} = \varphi^{-n}$, so $L_{2k} = \varphi^{2k} + \varphi^{-2k}$, **positive sign** → symmetric (bosonic)
- **$n$ odd** ($n = 2k+1$): $(-\varphi)^{-n} = -\varphi^{-n}$, so $L_{2k+1} = \varphi^{2k+1} - \varphi^{-(2k+1)}$, **negative sign** → antisymmetric (fermionic)

| Parity | Sign | Algebraic Meaning | Physical Meaning |
|:------:|:----:|:-----------------|:----------------|
| even $n$ | $+$ | symmetric | bosonic sector |
| odd $n$ | $-$ | antisymmetric | fermionic sector |

**Theorem 3 (Z₂ Selection Rule)**: In range 1-9, even-indexed Lucas numbers $\{L_0, L_2, L_4\} = \{2, 3, 7\}$ are forbidden by the Z₂ grading (symmetric/bosonic sector), while odd-indexed Lucas numbers $\{L_1, L_3\} = \{1, 4\}$ are allowed with $s=1$ (antisymmetric/fermionic sector).

### 4.2 Available Indices

After the Z₂ selection rule, available K-chain mode indices in 1-9:

$$\{1, 4, 5, 6, 8, 9\}$$

Skipped indices: $\{2, 3, 7\} = \{L_0, L_2, L_4\}$, sum $= 12 = 3 \times 4 = L_2 \times B$.

| $n$ | $F_n$ | Used? | $s$ |
|:---:|:-----:|:-----:|:---:|
| 1 | 1 | ✅ | 1 |
| 2 | 1 | ❌ | degenerate |
| 3 | 2 | ❌ | — |
| 4 | 3 | ✅ | 1 |
| 5 | 5 | ✅ | 2 |
| 6 | 8 | ✅ | 1 |
| 7 | 13 | ❌ | — |
| 8 | 21 | ✅ | 2 |
| 9 | 34 | ✅ | 3 |

---

## 5. Tree Depth Partition

### 5.1 Three Sectors

The K-tree has three sectors (Up, Down, Lepton), corresponding to three generations. This is determined by the MERA branching factor:

$$B = \varphi^3 - \varphi^{-3} = 4$$
$$N_{\text{sector}} = B - 1 = 3$$

### 5.2 Partition by Tree Depth

Six available indices divided by tree depth:

**Group A ($s=1$, focused)**: $\{1, 4, 6\}$, sum $= 11 = L_5$
**Group B ($s=2,3$, defocused)**: $\{5, 8, 9\}$, sum $= 22 = 2L_5$

Total: $33 = M = 3L_5 = 3 \times 11$

**Theorem 4 (Sum Partition)**: Group A sum = $L_5$, Group B sum = $2L_5$, total = $M = 3L_5$. This is a structural necessity of the $K = K_{\text{chain}} \otimes K_{\text{tree}}$ tensor product eigenvalue decomposition.

### 5.3 Sector-Specific Assignment

| Sector | $s=1$ idx | $F_n$ | $s=2,3$ idx | $F_n$ | Gap | $d$ |
|:-------|:---------:|:-----:|:-----------:|:-----:|:---:|:---:|
| Up | 1 | 1 | 9 | 34 | 8 | 3 |
| Down | 4 | 3 | 8 | 21 | 4 | 2 |
| Lepton | 6 | 8 | 5 | 5 | 1 | 0 |

---

## 6. Bipartite Graph: Uniqueness Proof

### 6.1 Problem Statement

Given two sets of indices:

$$A = \{1, 4, 6\}, \quad B = \{5, 8, 9\}$$

Find a bijection $f: A \to B$ satisfying:

1. **Gap condition**: $\Delta n = |b - a|$ must be $2^d$ (binary topological depth)
2. **Z₂ condition**: $\Delta n$ must NOT be an even-indexed Lucas number

### 6.2 Bipartite Graph

| $A \backslash B$ | 5 | 8 | 9 |
|:--------------:|:-:|:-:|:-:|
| **1** | $\Delta n=4=2^2$ ✅ | $\Delta n=7=L_4$ ❌ | $\Delta n=8=2^3$ ✅ |
| **4** | $\Delta n=1=2^0$ ✅ | $\Delta n=4=2^2$ ✅ | $\Delta n=5$ ❌ |
| **6** | $\Delta n=1=2^0$ ✅ | $\Delta n=2=L_0$ ❌ | $\Delta n=3=L_2$ ❌ |

**Allowed edges** (5): 1→5(4), 1→9(8), 4→5(1), 4→8(4), 6→5(1)
**Forbidden edges** (4): 1→8(7=L₄), 4→9(5), 6→8(2=L₀), 6→9(3=L₂)

### 6.3 Unique Bijection

**Unique solution**:

$$1 \xrightarrow{8} 9, \quad 4 \xrightarrow{4} 8, \quad 6 \xrightarrow{1} 5$$

**Proof**:
1. 6 only connects to 5 (unique neighbor) → $6 \to 5$ forced
2. 1 connects to $\{5, 9\}$, but 5 occupied → $1 \to 9$ forced
3. 4 connects to $\{5, 8\}$, but 5 occupied → $4 \to 8$ forced

**Theorem 5 (Pairing Uniqueness)**: The sector pairing is uniquely determined by the Z₂ selection rule and binary gap condition.

### 6.4 Depth Indices

| Sector | Pairing | Gap | $d = \log_2(\text{Gap})$ | Meaning |
|:-------|:-------:|:---:|:-------------------------:|:--------|
| Up | $1 \leftrightarrow 9$ | $8 = 2^3$ | **3** | Deepest, max splitting |
| Down | $4 \leftrightarrow 8$ | $4 = 2^2$ | **2** | Middle |
| Lepton | $6 \leftrightarrow 5$ | $1 = 2^0$ | **0** | Symmetry center, point-like |

---

## 7. Lepton Reversal: Z₂-Forced Topological Reflection

**Theorem 6 (Lepton Reversal)**: The Lepton pairing $6 \to 5$ is backward because the forward pairing $6 \to 7$ is forbidden by the Z₂ selection rule — $7 = L_4$ is an even-indexed Lucas number.

**Proof**:
1. From bipartite graph, 6's only allowed neighbor is 5 (6→8 blocked by 2=L₀, 6→9 blocked by 3=L₂)
2. If lepton followed forward pattern: $6 \to 6 + 1 = 7$
3. $7 = L_4$ is even-indexed Lucas → Z₂ forbidden
4. Only remaining index is 5
5. Therefore $6 \to 5$ (backward) forced

**Physical verification**: Forward to 7 gives F₇=13 → 13/134²=0.000724 (too large) or 13/134³=0.0000054 (too small). Actual F₅/134²=5/17956=0.000278 matches m_e/m_τ=0.000287 (3.1% error).

---

## 8. Sector Sum Symmetry

### 8.1 Centered on L₅

| Sector | $n_1 + n_2$ | Value | Deviation |
|:-------|:-----------:|:-----:|:---------:|
| Lepton | $6 + 5$ | **11** | $L_5$ (center) |
| Down | $4 + 8$ | **12** | $L_5 + 1$ |
| Up | $1 + 9$ | **10** | $L_5 - 1$ |

**Theorem 7 (Sector Sum Symmetry)**: $\{10, 11, 12\}$ is perfectly centered on $L_5 = 11$, corresponding to $\pm 1$ symmetry breaking. This is a natural consequence of the unique bijection, not an extra constraint.

### 8.2 Physical Meaning

Lepton as mass origin:
- **Symmetry axis**: $6+5 = 11 = L_5$
- **No color charge**: sits on symmetry axis, no $\pm 1$ needed
- **Min gap**: $2^0 = 1$, at tree root
- **Zero correction**: IR pinned

Up and Down as symmetry breaking:
- **Up**: $-1$ deviation, deepest tree ($33\beta$), max gap ($8$), $d=3$
- **Down**: $+1$ deviation, middle tree ($26\beta$), mid gap ($4$), $d=2$, has Casimir term

---