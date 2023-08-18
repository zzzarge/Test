-- SELECT 
--     book.id,    
--     book.name,
--     CONCAT(author.name, " ", author.surname) as author,
--     genre.name as genre
-- FROM book
--     JOIN author ON author.id = book.author_id
--     JOIN genre ON genre.id = book.genre_id
-- ORDER BY author.name;


-- SELECT
--     cart_product.cart_id,
--     book.name,
--     book.price
-- FROM cart_product
--     LEFT JOIN book ON book.id = cart_product.book_id
-- WHERE cart_product.cart_id = 1;
    

-- SELECT
--     cart_product.cart_id,
--     CONCAT(customer.name, " ", customer.surname) as customer,
--     book.name,
--     book.price,
--     cart_product.quantity,
--     book.price * cart_product.quantity as total
-- FROM cart_product
--     LEFT JOIN book ON book.id = cart_product.book_id
--     LEFT JOIN cart ON cart.id = cart_product.cart_id
--     LEFT JOIN customer ON customer.id = cart.customer_id
-- ORDER BY customer.id;


-- ALTER TABLE cart RENAME COLUMN customer TO customer_id;

-- SELECT
--     cart_product.cart_id,
--     CONCAT(customer.name, " ", customer.surname) as customer,
--     book.name,
--     book.price,
--     cart_product.quantity,
--     (book.price * cart_product.quantity) as total
-- FROM cart_product
--     LEFT JOIN book ON book.id = cart_product.book_id
--     LEFT JOIN cart ON cart.id = cart_product.cart_id
--     LEFT JOIN customer ON customer.id = cart.customer_id
-- WHERE book.price * cart_product.quantity > 500;


-- SELECT 
--     genre.name,
--     SUM(cart_product.quantity) as quantity,
--     SUM(book.price) as total
-- FROM cart_product
--     LEFT JOIN book ON book.id = cart_product.book_id
--     LEFT JOIN genre ON genre.id = book.genre_id
-- GROUP BY book.genre_id;

SELECT 
    customer.id,
    CONCAT(customer.name, " ", customer.surname) as full_name,
    SUM(book.price * cart_product.quantity) as total
FROM cart_product
    LEFT JOIN book ON book.id = cart_product.book_id
    LEFT JOIN cart ON cart.id = cart_product.cart_id
    LEFT JOIN customer ON customer.id = cart.customer_id
GROUP BY customer.id;