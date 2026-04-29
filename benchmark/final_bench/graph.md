C1: задача классификации

C2: бинарная классификация

C3: классификация на $K$ классов

C4: таргет $y$

C5: положительный класс

C6: отрицательный класс

C7: множество $\{-1, 1\}$

C8: признак $x_i$

C9: вектор

C10: пространство $\mathbb{R}^D$

C11: линейная модель

C12: веса $w$

C13: разделяющая плоскость

C14: выборка

C15: линейная разделимость

C16: предсказание $\hat{y}$

C17: $\hat{y}=\operatorname{sign}\langle w, x_i\rangle$

C18: регрессия

C19: MSE

C20: функционал ошибки классификатора

C21: число ошибок классификатора

C22: $\sum_i [y_i\langle w, x_i\rangle < 0]\to\min_w$

C23: отступ $M=y_i\langle w, x_i\rangle$

C24: положительный отступ

C25: отрицательный отступ

C26: $F(M)=[M<0]=\begin{cases}1, & M<0, \\ 0, & M\ge 0.\end{cases}$

C27: ошибка перцептрона

C28: $L(w,x,y)=\lambda\|w\|_2^2+\sum_i\max(0,-y_i\langle w,x_i\rangle)$

C29: $\nabla_w L(w,x,y)=2\lambda w+\sum_i\begin{cases}0, & y_i\langle w,x_i\rangle>0, \\ -y_i x_i, & y_i\langle w,x_i\rangle\le 0.\end{cases}$

C30: стохастический градиентный спуск

C31: hinge loss

C32: $L(w,x,y)=\lambda\|w\|_2^2+\sum_i\max(0,1-y_i\langle w,x_i\rangle)$

C33: $\nabla_w L(w,x,y)=2\lambda w+\sum_i\begin{cases}0, & 1-y_i\langle w,x_i\rangle\le 0, \\ -y_i x_i, & 1-y_i\langle w,x_i\rangle>0.\end{cases}$

C34: минимальный отступ

C35: ширина полосы $\dfrac{2}{\|w\|_2}$

C36: логистическая регрессия

C37: классы $\{0,1\}$

C38: вероятность $p$

C39: логит $\log\left(\dfrac{p}{1-p}\right)$

C40: $\langle w,x_i\rangle=\log\left(\dfrac{p}{1-p}\right)$

C41: $p=\dfrac{1}{1+e^{-\langle w,x_i\rangle}}$

C42: сигмоида $\sigma(z)=\dfrac{1}{1+e^{-z}}$

C43: правдоподобие $p(y\mid X,w)$

C44: распределение Бернулли

C45: $p(y\mid X,w)=\prod_i p(y_i\mid x_i,w)$

C46: $p(y\mid X,w)=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}$

C47: вероятность $p_i$

C48: функция потерь $L(w,X,y)$

C49: $L(w,X,y)=-\sum_i\left(y_i\log(\sigma(\langle w,x_i\rangle))+(1-y_i)\log(\sigma(-\langle w,x_i\rangle))\right)$

C50: $\nabla_w L(y,X,w)=-\sum_i x_i\left(y_i-\sigma(\langle w,x_i\rangle)\right)$

C51: диапазон $[0,1]$

C52: порог классификации

C53: отложенная тестовая выборка

C54: разделяющая поверхность

C55: гиперплоскость

R1: "является частным случаем"
  subject: C2
  object: C1

R2: "обобщается до"
  subject: C2
  object: C3

R3: "кодирует принадлежность к"
  subject: C4
  object: C5

R4: "кодирует принадлежность к"
  subject: C4
  object: C6

R5: "принимает значения из"
  subject: C4
  object: C7

R6: "является"
  subject: C8
  object: C9

R7: "принадлежит"
  subject: C9
  object: C10

R8: "параметризуется"
  subject: C11
  object: C12

R9: "задаёт"
  subject: C11
  object: C13

R10: "разделяет классы в"
  subject: C13
  object: C2

R11: "может обладать свойством"
  subject: C14
  object: C15

R12: "определяется как"
  subject: C16
  object: C17

R13: "использует"
  subject: C17
  object: C12

R14: "использует"
  subject: C17
  object: C8

R15: "может быть наивным подходом к"
  subject: C18
  object: C1

R16: "минимизирует"
  subject: C18
  object: C19

R17: "является плохим подходом для"
  subject: C18
  object: C1

R18: "минимизирует"
  subject: C20
  object: C21

R19: "записывается как"
  subject: C20
  object: C22

R20: "использует"
  subject: C22
  object: C23

R21: "может быть"
  subject: C23
  object: C24

R22: "может быть"
  subject: C23
  object: C25

R23: "вычисляется от"
  subject: C26
  object: C23

R24: "является"
  subject: C27
  object: C28

R25: "имеет градиент"
  subject: C27
  object: C29

R26: "оптимизируется методом"
  subject: C27
  object: C30

R27: "является"
  subject: C31
  object: C32

R28: "имеет градиент"
  subject: C31
  object: C33

R29: "оптимизируется методом"
  subject: C31
  object: C30

R30: "максимизирует"
  subject: C31
  object: C34

R31: "соответствует"
  subject: C34
  object: C35

R32: "обозначает классы как"
  subject: C36
  object: C37

R33: "предсказывает"
  subject: C36
  object: C38

R34: "связана с"
  subject: C38
  object: C39

R35: "задаётся равенством"
  subject: C40
  object: C39

R36: "вычисляется как"
  subject: C38
  object: C41

R37: "является значением"
  subject: C41
  object: C42

R38: "подбираются через максимизацию"
  subject: C12
  object: C43

R39: "основано на"
  subject: C43
  object: C44

R40: "определяется как"
  subject: C43
  object: C45

R41: "для распределения Бернулли равно"
  subject: C43
  object: C46

R42: "является"
  subject: C47
  object: C38

R43: "получается из"
  subject: C48
  object: C43

R44: "равна"
  subject: C48
  object: C49

R45: "минимизируется для подбора"
  subject: C48
  object: C12

R46: "имеет градиент"
  subject: C48
  object: C50

R47: "находится в"
  subject: C38
  object: C51

R48: "определяет принадлежность к"
  subject: C52
  object: C5

R49: "подбирается по"
  subject: C52
  object: C53

R50: "задаёт"
  subject: C36
  object: C54

R51: "является"
  subject: C54
  object: C55
