
### Indexing:

Unorganized things take O(n) time to search a thing from them 
like finding a number from an unordered array

you will have to do linear search in worst case and it will take O(n)

For a sorted array .. you can use binary search .. and you get O(log n)



For a normal table .. you do search using 
~ select * from emp where salary > 4000;
it takes time and is slow for worst case


we can add indexing on salary column so that our queries can go faster

in indexing .. a column remains same (unordered/ordered in the same table)
but on a new location/memory the same column is sorted for fast search/filter

this separate column also has a pointer pointing to old tables column 

so on where clause it doesn't filter/search from the same table but checks if it has indexing then search from that whihc will be much faster 

### How to optimize a table for faster search?
`Indexing creates a lookup table with the column and the pointer to the memory location of the row, containing this column.`

`Indexing makes it O(log n)`

### Which Data strcuture?
`B-Tress are used for indexing -  a balanced binary search tress`

### Where to use?
`We use indexing for Read Intensive databse tables.. tables which have too many read requests`

### Where to not use?
`Otherwise you shouldn't.. like in case of update or write intensive.. you will have to add/update a value in the table alongside the indexed table`

