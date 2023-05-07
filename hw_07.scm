; Вопрос 1
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

; Вопрос 2
(define (sign x)
  (cond
    ((> x 0) 1)
    ((< x 0) -1)
    (else 0)
  )
)

; Вопрос 3
(define (square x) (* x x))

(define (pow b n)
  (cond
    ((= n 1) b)
    ((even? n) (square (pow b (/ n 2))))
    ((odd? n) (* b (square (pow b (/ (- n 1) 2)) )))
  )
)

; Вопрос 4
(define (ordered? s)
  (cond
   ((= (length s) 0) #t)
   ((= (length s) 1) #t)
   ((ordered? (cdr s)) (<= (car s) (car (cdr s))))
   (else #f) 
  )  
)

; Вопрос 5
(define (empty? s) (null? s))

(define (add s v)
(cond 
((> (car s) v) (if (empty? (cdr s)) (cons v (cons (car s) nil)) (cons v (add (cdr s) (car s) ))))
((= (car s) v) (add (cdr s) v) )
((< (car s) v) (if (empty? (cdr s)) (cons (car s) (cons v nil)) (cons (car s) (add (cdr s) v))))
)
)
; Вопрос 6
(define (contains? s v)
  (cond
    ((empty? s) #f)
    ((= (car s) v) #t)
    (else (contains? (cdr s) v))
  )
)

; Эквивалентный код на Python:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

; Вопрос 7
(define (intersect s t)
  (cond
   ((empty? s) nil)
   ((empty? t) nil)
   ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
   ((< (car s) (car t)) (intersect (cdr s) t))
   ((> (car s) (car t)) (intersect s (cdr t)))
  )
)

; Эквивалентный код на Python:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  (cond 
    ((< (length s) (length t))  (union t s))
    ((empty? s) nil)
    ((not (empty? t))
      (cond  
        ( (< (car s) (car t)) (cons (car s) (union (cdr s) t)) )
        ( (> (car s) (car t)) (cons (car t) (union s (cdr t))) ) 
        ( (= (car s) (car t)) (cons (car t) (union (cdr s) (cdr t)))) 
      )
    )
    ( (empty? t) (cons (car s) (union (cdr s) t)))  
  )

)
