(define-macro (for x lst expr)
                (list 'map (list 'lambda (list x) expr) lst))


(define-macro (list-of map-expr for var in lst . iff)
  ;(for var (filter f? lst) map-expr) ;решение
  ;(define var x)
  (if (null? iff) 
    (list for var lst map-expr)
    (list 'for var (list 'filter (list 'lambda (list var) (car (cdr iff))) lst) map-expr)
  )
)

  