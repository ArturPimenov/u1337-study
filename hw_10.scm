
; Хвостовая рекурсия
; Вопрос 1
(define (replicate x n . lst_x)
  (if (= n 0) (if (null? lst_x) lst_x (car lst_x)) 
              (if (null? lst_x) (replicate x (- n 1) (append lst_x `(,x))) (replicate x (- n 1) (append (car lst_x) `(,x))))
  )
)

; Вопрос 2
(define (accumulate combiner start n term)
(if (= n 0) start (combiner (term n) (accumulate combiner start (- n 1) term)))
)

; Вопрос 3
(define (accumulate-tail combiner start n term . result) 
  (if (= n 0) (if (null? result) result (combiner (term start) (car result)))
                                 (if (null? result) (accumulate-tail combiner n (- n 1) term start)
                                                    (accumulate-tail combiner n (- n 1) term (combiner (term start) (car result))))
              )
)

; Потоки
; Вопрос 4
(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define (int n) (cons-stream n (int (+ n 1))))

(define multiples-of-three
  (let ((int_1 (int 1)))  
  (map-stream (lambda (x) (* x 3)) int_1)
  )
)

; Вопрос 5
(define (up_subs stream) 
    (cond ((null? stream) nil)
          ((null? (cdr-stream stream)) (cons (car stream) (up_subs (cdr-stream stream))))
          ( (> (car stream) (car (cdr-stream stream))) (cons (car stream) nil) )
          (else (cons (car stream) (up_subs (cdr-stream stream))))
    )    
)

(define (next_stream stream)
    (cond ((null? stream) nil)
          ((null? (cdr-stream stream)) nil)
          ( (> (car stream) (car (cdr-stream stream))) (cdr-stream stream))
          (else (next_stream (cdr-stream stream)))
    )   
)

(define (nondecreastream s)
    (let ((lst (up_subs s)) (next (next_stream s)))
         (if (null? next) (cons-stream lst nil) (cons-stream lst (nondecreastream next)))
    )     

)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))