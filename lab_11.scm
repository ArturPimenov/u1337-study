; Вопрос 3
(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            ((y (repeatedly-cube (- n 1) x)))
            (* y y y))))

; Вопрос 4
(define-macro (def func bindings body)
    `(define ,(eval `(cons ',func ',bindings)) ,body)  
)

; Вопрос 5
(define-macro (switch expr cases)
    (define (f lst) (if (eq? (car lst) (eval expr)) (car (cdr (eval (car (cdr `(,eval lst))))))))
    (car (cdr (car (filter f cases))))     
)


; Вопрос 6
(define (flatmap f x . lstnak)
    (if (null? x) 
        ;nil
        (if (null? lstnak) lstnak (car lstnak))
        (let ( (lst (f (car x))) )
                (if (list? lst)
                    ;(append lst (flatmap f (cdr x)))
                    (if (null? lstnak) (flatmap f (cdr x) (append lstnak lst)) (flatmap f (cdr x) (append (car lstnak) lst)))
                    ;(cons lst (flatmap f (cdr x)))
                    (if (null? lstnak) (flatmap f (cdr x) (append lstnak (list lst))) (flatmap f (cdr x) (append (car lstnak) (list lst))))
                )
        )    
    )
)

(define (expand lst)
    (flatmap 
        (lambda (x) 
            (cond ((eq? x 'x) '(x r y f r))
                  ((eq? x 'y) '(l f x l y))
                  (else x)
            )
        ) 
        lst)
)

(define (interpret instr dist)
    (cond ((null? instr) nil)
          ((eq? (car instr) 'f) (begin (forward dist) (interpret (cdr instr) dist)))
          ((eq? (car instr) 'l) (begin (left 90) (interpret (cdr instr) dist)))
          ((eq? (car instr) 'r) (begin (right 90) (interpret (cdr instr) dist)))
          (else (interpret (cdr instr) dist)) 
    )    
)

(define (apply-many n f x)
  (if (zero? n)
      x
      (apply-many (- n 1) f (f x))))

(define (dragon n d)
  (interpret (apply-many n expand '(f x)) d))